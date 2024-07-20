from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import logging
import stripe
import requests
import json
import os
from django.db.models import Q
from inventory.models import Inventory, StripeProduct
import decimal
import argparse


class Command(BaseCommand):
    help = "Handles various operations on inventory items"
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.dirname(os.path.dirname(current_dir))
    config = json.load(open(f"{app_dir}/config.json"))

    logging.basicConfig(
        filename="error_log.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "action",
            type=str,
            help="Action to perform: convert_to_dec, editconfig, pushUpdates",
        )

    def handle(self, *args, **kwargs):
        action = kwargs["action"]

        if action == "convert_to_dec":
            self.convert_to_decimal()
        elif action == "init":
            self.initialization()

        elif action == "import_to_stripe":
            self.import_to_stripe()
        elif action == "update_prices_from_ebay":
            self.update_prices_from_ebay()
        elif action == "test":
            self.test()
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Unknown action. Use one of: convert_to_dec, editconfig, pushUpdates"
                )
            )

    def initialization(self):
        if (
            not self.config["Django"]["DJANGO_SECRET_KEY"]
            or self.config["Django"]["DJANGO_SECRET_KEY"] == ""
        ):
            self.config["Django"]["DJANGO_SECRET_KEY"] = get_random_secret_key()
        with open(f"{app_dir}/config.json", "w") as conf:
            json.dump(self.config, f, indent=4)

    def convert_to_decimal(self):
        for item in Inventory.objects.all():
            try:
                item.price = decimal.Decimal(item.price)
                item.save()
            except (ValueError, decimal.InvalidOperation):
                # Handle or log conversion errors
                item.price = None
                item.save()

        self.stdout.write(self.style.SUCCESS("Conversion completed successfully"))

    def update_prices_from_ebay(self):
        headers = {
            "Authorization": f"Bearer {self.config['Production']['Oauth']}",
            "Accept": "application/json",
        }
        # ending 364817714570
        existing_ebay_items = Inventory.objects.exclude(
            Q(ebay_itemid=True) | Q(ebay_itemid="")
        )

        # print("number of items:" , len(existing_ebay_items))
        print(self.config["Production"]["Oauth"])
        for x in existing_ebay_items[80:200]:
            print("Processing: ", x.ebay_itemid, ":", x.full_title)
            endpoint = f"https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?legacy_item_id={x.ebay_itemid}"
            response = requests.get(endpoint, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                print(
                    f"""
                    itemID: {data["itemId"].split("|")[-2]}
                    category: {data["categoryPath"].split("|")[-1]}
                    categoryID: {data["categoryIdPath"].split("|")[-1]}
                    price: {data['price']['value']}
                    """
                )
                item = {
                    "itemID": data["itemId"].split("|")[-2],
                    "category": data["categoryPath"].split("|")[-1],
                    "categoryID": data["categoryIdPath"].split("|")[-1],
                    "price": data["price"]["value"],
                }
                db_items = Inventory.objects.filter(ebay_itemid=x.ebay_itemid)
                for db_item in db_items:
                    db_item.price = float(item["price"])
                    db_item.save()
                    print(
                        f"{x.ebay_itemid}:{x.full_title}, has been saved for ${item['price']}!"
                    )

            else:
                # Print an error message if the request was not successful
                print(f"Error: {response.status_code} - {response.text}")
                error = {"code": response.status_code, "message": response.text}

    def import_to_stripe(self):
        stripe.api_key = self.config["Stripe"]["SecretKey"]
        print(stripe.api_key)
        existing_items = list(
            Inventory.objects.exclude(Q(ebay_itemid=True) | Q(ebay_itemid=""))
        )

        for idx, item in enumerate(existing_items[104:]):
            try:
                stripe_product = stripe.Product.create(
                    name=item.full_title,
                    description=item.description if item.description else "product",
                    #   object="product",
                    images=[item.picurl]
                    if ("|") not in item.picurl
                    else [item.picurl.split("|")[0]],
                    package_dimensions={
                        "height": item.package_height,
                        "length": item.package_length,
                        "width": item.package_width,
                        "weight": item.package_weight,
                    },
                    tax_code="txcd_99999999",
                )

                stripe_price = stripe.Price.create(
                    unit_amount=int(item.price * 100),
                    currency="usd",
                    product=stripe_product["id"],
                )

                spdb_item = StripeProduct.objects.create(
                    product_id=stripe_product["id"],
                    item_id=item,
                    name=stripe_product["name"],
                    unit_amount=stripe_price["unit_amount"],
                    currency=stripe_price["currency"],
                    description=stripe_product["description"],
                    is_active=stripe_price["active"],
                    created_at=stripe_product.created,
                    updated_at=stripe_product.updated,
                    images=stripe_product["images"][0],
                )
            except stripe.error.StripeError as e:
                print(
                    f"Stripe API Error: index: {idx} item: {item.item_id} - {item.full_title}\n{e}"
                )
                logging.error(
                    f"Stripe API Error: index: {idx} item: {item.item_id} - {item.full_title}\n{e}"
                )

            except Exception as e:
                print(
                    f"Error: index: {idx} inventory item: {item.item_id} - {item.full_title}\n{e}"
                )
                logging.error(
                    f"Error: index: {idx} inventory item: {item.item_id} - {item.full_title}\n{e}"
                )

            # print("stripe_product:", stripe_product)
            # print("stripe_price:", stripe_price)
            # for field, value in spdb_item.__dict__.items():
            #     if not field.startswith('_'):
            #         print(f"{field}: {value}")

        # for item in existing_items:
        #     product = {

        #     }

    def test(self):
        existing_items = list(
            Inventory.objects.exclude(Q(ebay_itemid=True) | Q(ebay_itemid=""))
        )
        index = 0
        for idx, item in enumerate(existing_items):
            if item.item_id == 105:
                index = idx
        print("Index stopped at: ", index)
