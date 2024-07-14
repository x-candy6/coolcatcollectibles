import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.authtoken.models import Token

from . import models

# Create your views here.

def get_user_from_access_token(access_token_str):
    try:
        # Decode the access token
        access_token = AccessToken(access_token_str)
        
        # Verify the access token
        access_token.verify()
        
        # Extract user id from the access token payload
        user_id = access_token.payload['user_id']
        
        # Fetch user object using the user_id
        user = User.objects.get(id=user_id)
        
        return user
    
    except InvalidToken:
        print("Invalid access token")
        return None
    except User.DoesNotExist:
        print("User not found")
        return None
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return None

def getGeneralInventory(request, token):

    try:
        user = get_user_from_access_token(token)
        print(user.id)
        #items = models.Inventory.objects.filter(user=user.id)
        items = models.Inventory.objects.filter(listing_title__icontains="Catwoman")  
        headers = [field.name for field in items.first()._meta.fields]

        inventory = {
            'headers' : headers,
            'inventory': list(items.values())
        }
        #print(inventory)

        return JsonResponse(inventory, status=200)
    except Token.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=401)
    return

@csrf_exempt
def updateInventoryItem(request):
    print('running updateInventoryItem')
    # try:
    #     user = get_user_from_access_token(token)
    # except:
    #     return JsonResponse({'error': 'Invalid User'}, status=401)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("updating item:", data)
            item_id = data.get('item_id')
            column_name = data.get('column_name')
            print(column_name)
            new_value = data.get('new_value')
            #print(item_id, column_name, new_value)

            item = models.Inventory.objects.get(item_id=item_id)
            setattr(item, column_name, new_value)
            item.save()
            msg = f"{column_name} of inventory item with pk={item_id} updated to '{new_value}'."
            return JsonResponse({'message': msg}, status=200)
        except: 
            return JsonResponse({'error':'Item not updated'}, status=400)

@csrf_exempt
def searchInventory(request, category, query):
    
    if request.method == 'GET':
        # TODO: Perform token validation
        
        # Filter the inventory based on category and query
        if category and query:
            filter_criteria = {f"{category}__icontains": query}
            search_results = models.Inventory.objects.filter(**filter_criteria)

        else:
            search_results = models.Inventory.objects.all()

        # Convert the results to a list of dictionaries
        inventory_list = list(search_results.values())
        print(inventory_list)

        response_data = {
            'inventory': inventory_list
        }

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def getItem(request, itemID):
    if request.method == 'GET':
        print(itemID)
        if itemID:
            product = models.Inventory.objects.get(item_id=itemID)
        else:
            return JsonResponse({'error': 'Error retrieving product'}, status=400)
        
        response_data ={
            'product': model_to_dict(product)
        }
        return JsonResponse(response_data, status=200)


def parse_price_range(price_range):
    # Implement logic to parse and return min and max prices from a string input
    # Example: "10-50" => (10, 50)
    min_price, max_price = map(float, price_range.split('-'))
    return min_price, max_price

# API /inventory/api/catalog/$CATEGORY/$VALUE

@csrf_exempt
def getCatalog(request, category=None, query=None):
    print("category:", category)
    print("query:", query)

    if request.method == 'GET':
        # Potentially taxxing on server requests?
        product_list = models.Inventory.objects.all()

        filters = {}
        # filters = {
        #     "priceRange" : request.GET.get('priceRange'),
        #     "publisher" : request.GET.get('publisher'),
        #     "era" : request.GET.get('era'),
        #     "years" : request.GET.get('years'),
        #     "characters" : request.GET.get('character') # adjust to allow for multiple characters,
        # }

        if category == "publishers":
            if query:
                product_list = product_list.filter(publisher__icontains=query)
            else:
                product_list = product_list.exclude(publisher__isnull=True)
        elif category == "timeera":
            if query:
                product_list = product_list.filter(time_era__icontains=query)
            else:
                return JsonResponse({'message': 'Time era query not provided'}, status=400)

        # Add more elif blocks for other categories as needed
        # elif category == "category_name":
        #     if query:
        #         product_list = product_list.filter(field__icontains=query)
        #     else:
        #         return JsonResponse({'message': 'Category query not provided'}, status=400)

        # Apply additional filters from query parameters
        price_range = request.GET.get('priceRange')
        if price_range:
            filters['price_range'] = parse_price_range(request.GET.get('priceRange'))
            print(filters['price_range'])
        if request.GET.get('publisher'):
            filters['publisher'] = request.GET.get('publisher')
        if request.GET.get('era'):
            filters['time_era'] = request.GET.get('era')

        # Add more filters based on query parameters similarly

        if filters:
            if filters.get('price_range'):
                product_list = product_list.filter(price__range=filters['price_range'])
                print(product_list)
            if filters.get('publisher'):
                product_list = product_list.filter(publisher=filters['publisher'])
            if filters.get('time_era'):
                product_list = product_list.filter(time_era=filters['time_era'])
                #product_list = product_list.filter(**filters)

            # TODO 
            # if filters.get('character'):
            # if filters.get('years'):

        # Pagination logic
        page_number = request.GET.get('page', 1)
        paginator = Paginator(product_list, 10)  # Adjust the page size as needed
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        response_data = {
            'products': list(products.object_list.values()),
            'current_page': products.number,
            'total_pages': paginator.num_pages,
            'has_next': products.has_next(),
            'has_previous': products.has_previous(),
        }

        return JsonResponse(response_data, status=200)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)