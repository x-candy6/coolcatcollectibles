from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, alogin
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

import json
from . import models

@csrf_exempt
def issue_session_token(request):

    session = models.Session.objects.create()
    print(session.sessionid)

    # TODO if user is authenticated, set the userID parameter
    session_token = RefreshToken()

    access_token = str(session_token.access_token)
    refresh_token = str(session_token)

    session_token['sessionid'] = session.sessionid
    return JsonResponse({
        'session_id': session.sessionid,
        "access_token": access_token,
        "refresh_token": refresh_token
    }, status=200)

@api_view(['GET'])
@csrf_exempt
def validate_session_token(request):

    # Get Token
    access_token = request.headers.get('session-access-token')
    print(access_token)
    # No Token Found
    if access_token == "undefined":
        print('No access token found in headers...')
        return JsonResponse({'error': 'No token found.'}, status=404)
    try:
        # Validate Token
        access_token = AccessToken(access_token)

        #if access_token.is_expired: # Check if expired
        #    return JsonResponse({'error': 'Expired token.'}, status=401)

    except (TokenError) as e: # Invalid Token
        return JsonResponse({'error': f'TokenError'}, status=400)
    except (InvalidToken) as e: # Invalid Token
        return JsonResponse({'error': f'Invalid Token'}, status=400)


    # Token is valid
    return JsonResponse({'message': 'Token is valid.'}, status=200)

@csrf_exempt
def refresh_session_token(request):
    refresh_token = request.headers.get('session-refresh-token')
    session_id = request.headers.get('session-id')
    print("session_id:", session_id)
    if session_id:
        update_session = models.Session.objects.get(sessionid = session_id)
        try:
            refresh = RefreshToken(refresh_token)
        except:
            refresh = RefreshToken()
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        update_session.access_token = access_token
        update_session.refresh_token = refresh_token
        update_session.save()
        print("refresh_session_token, session_id:", session_id)

        return JsonResponse({
            'session_id': session_id,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, status=200)

    if refresh_token == "undefined":
        return JsonResponse({'error': 'No refresh token found.'}, status=404)

    refresh = RefreshToken(refresh_token)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return JsonResponse({
        'session_id': session_id,
        "access_token": access_token,
        "refresh_token": refresh_token
    }, status=200)


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

def getUserData(request, token):
    try:
        user = get_user_from_access_token(token)

        user_data = {
            'token': token,
            'username': user.username,
            # Include other user data as needed
        }

        return JsonResponse(user_data, status=200)
    except Token.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=401)


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if not (username and email and password):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username is already taken'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        models.Profile.objects.create(id=user).save()

        refresh = RefreshToken.for_user(user)

        # Serialize user and token data into dictionary
        user_data = {
            # 'token': token.key,
            # 'token_created': token_created,
            'token': str(refresh.access_token),
            'username': user.username,
            'userid': user.id
            # Include other user data as needed
        }

        return JsonResponse(user_data, status=200)


        # Insert code for all post operations here...

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Generate JWT token
            refresh = RefreshToken.for_user(user)

            # Serialize user and token data into dictionary
            user_data = {
                'token': str(refresh.access_token),
                'username': user.username,
                'userid': user.id
                # Include other user data as needed
            }

            return JsonResponse(user_data, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': "Logout successful. "}, status=200)


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sessionID = models.Session.objects.get(sessionid=data.get('sessionID'))
        itemID = data.get('itemID')
        qty = data.get('qty')
        print(sessionID, itemID, qty)

        # add try/except block
        retrievedProduct = models.Inventory.objects.get(item_id=itemID)
        print(retrievedProduct.full_title)

        # Retrieve/create cart associated with session if exists
        guest_cart, created = models.GuestCart.objects.get_or_create(session_id=sessionID)

        guest_cart_item, created = models.GuestCartItems.objects.get_or_create(
            product_id=retrievedProduct,
            guest_cart_id = guest_cart,
            session_id=sessionID  # change to fk instead of hardcoded value
        )
        if not created:
            guest_cart_item.qty=qty
            guest_cart_item.save()
        else:
            guest_cart_item.qty = qty
            guest_cart_item.save()

    return JsonResponse({'message': "Added item to cart. "}, status=200)

@csrf_exempt
def remove_from_cart(request):
    return JsonResponse({'message': "Logout successful. "}, status=200)

@csrf_exempt
def update_cart(request):
    return JsonResponse({'message': "Logout successful. "}, status=200)

@csrf_exempt
def merge_cart(request):
    return JsonResponse({'message': "Logout successful. "}, status=200)

@api_view(['GET'])
@csrf_exempt
def get_cart(request):
    print("getting cart...")
    print(request.headers['session-id'])
    sessionID = models.Session.objects.get(sessionid=request.headers['session-id'])
    cart = models.GuestCart.objects.get(session_id=sessionID.sessionid)
    raw_cart_items = models.GuestCartItems.objects.filter(guest_cart_id=cart.guest_cart_id)
    cart_items = []

    for item in raw_cart_items:
        product = models.Inventory.objects.get(item_id=item.product_id_id)
        cart_items.append({
            'id': product.item_id,
            'title': product.full_title,
            'quantity': item.qty,
            'price': float(product.price),
            'image': product.picurl
        })
    


    return JsonResponse({'cart_items':cart_items}, safe=False,status=200)
