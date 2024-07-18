from django.conf import settings
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
from inventory import models
import stripe

def get_price_id(product_id):
    prices = stripe.Price.list(product=product_id)
    
    price_ids = [price.id for price in prices.data]
    price_ids = price_ids[0]
    
    return price_ids
    
@csrf_exempt
def stripe_checkout(request):
    try:

        if request.method == 'POST':
            data = json.loads(request.body)
            req_cart_items = data.get('line_items')
            cart_items = []

            for item in req_cart_items:
                product = models.Inventory.objects.filter(item_id=item['id'])[0]
                stripe_product = models.StripeProduct.objects.filter(item_id=product.item_id)[0]
                print(stripe_product.product_id)
                price_id = get_price_id(stripe_product.product_id)
                cart_items.append({
                    'price': price_id,
                    "quantity": item['quantity']
                })

            for item in cart_items:
                print("item: ", item)

            success_url= settings.DOMAIN_NAME + '/checkout/stripe/success',
            print(success_url)
            checkout_session = stripe.checkout.Session.create(
                line_items = cart_items,
                mode='payment',
                success_url= "http://" + settings.DOMAIN_NAME + '/checkout/stripe/success',
                cancel_url= "http://" + settings.DOMAIN_NAME + '/checkout/stripe/cancel',
                automatic_tax={'enabled': True}
            )

    except Exception as e:
        print(str(e))
        return JsonResponse({}, status=400)

    return JsonResponse({"checkout_session_url":checkout_session.url}, status=303)

