from django.core.management.base import BaseCommand
import requests
import json
import os
from django.db.models import Q
from inventory.models import Inventory
import decimal
import argparse

class Command(BaseCommand):
    help = 'Handles various operations on inventory items'
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.dirname(os.path.dirname(current_dir))
    config = json.load(open(f"{app_dir}/config.json"))

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help='Action to perform: convert_to_dec, editconfig, pushUpdates')

    def handle(self, *args, **kwargs):
        action = kwargs['action']
        
        if action == 'convert_to_dec':
            self.convert_to_decimal()

        elif action == 'temp_price_update':
            self.temp_price_update()
        elif action == 'update_prices_from_ebay':
            self.update_prices_from_ebay()
        else:
            self.stdout.write(self.style.WARNING('Unknown action. Use one of: convert_to_dec, editconfig, pushUpdates'))

    def convert_to_decimal(self):
        for item in Inventory.objects.all():
            try:
                item.price = decimal.Decimal(item.price)
                item.save()
            except (ValueError, decimal.InvalidOperation):
                # Handle or log conversion errors
                item.price = None
                item.save()

        self.stdout.write(self.style.SUCCESS('Conversion completed successfully'))

    def update_prices_from_ebay(self):
        headers = {
            "Authorization": f"Bearer {self.config['Production']['Oauth']}",
            "Accept": "application/json"
        }
        # ending 364817714570
        existing_ebay_items = Inventory.objects.exclude(Q(ebay_itemid=True) | Q(ebay_itemid=''))
        #print("number of items:" , len(existing_ebay_items))
        print(self.config['Production']['Oauth'])
        for x in existing_ebay_items[:2]:
            print("Processing: ", x.ebay_itemid, ":", x.full_title)
            endpoint = f"https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?legacy_item_id={x.ebay_itemid}"
            response = requests.get(endpoint, headers=headers)
    
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                print(
                    f'''
                    itemID: {data["itemId"].split("|")[-2]}
                    category: {data["categoryPath"].split("|")[-1]}
                    categoryID: {data["categoryIdPath"].split("|")[-1]}
                    price: {data['price']['value']}
                    '''
                )
                item = {
                    "itemID": data["itemId"].split("|")[-2],
                    "category": data["categoryPath"].split("|")[-1],
                    "categoryID": data["categoryIdPath"].split("|")[-1],
                    'price': data['price']['value']
                }
                db_items = Inventory.objects.filter(ebay_itemid=x.ebay_itemid)
                for db_item in db_items:
                    db_item.price = float(item['price'])
                    db_item.save()
                    print(f"{x.ebay_itemid}:{x.full_title}, has been saved for ${item['price']}!")
    
            else:
                # Print an error message if the request was not successful
                print(f"Error: {response.status_code} - {response.text}")
                error = {
                    "code": response.status_code,
                    "message": response.text
    
                }

    def temp_price_update(self):
        last_item_updated = 364817714570
        pre_existing_ebay_items = list(Inventory.objects.exclude(Q(ebay_itemid=True) | Q(ebay_itemid='')))
        index = 0

        #print("number of items:" , len(existing_ebay_items))
        for i, item in enumerate(pre_existing_ebay_items):
            if item.ebay_itemid == last_item_updated:
                index = i
                break
        print(index)

        #existing_ebay_items = pre_existing_ebay_items[index + 1:]

        for x in pre_existing_ebay_items:
                db_items = Inventory.objects.filter(ebay_itemid=x.ebay_itemid)
                for db_item in db_items:
                    db_item.price = float(9.99)
                    db_item.save()
                    print(f"{x.ebay_itemid}:{x.full_title}, has been saved for ${db_item.price}!")
    
    

