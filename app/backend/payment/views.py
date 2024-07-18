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
import stripe

@csrf_exempt
def stripe_checkout(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            line_items = data.get('line_items')
            checkout_session = stripe.checkout.Session.create(
                line_items = line_items,
                mode='payment',
                success_url= settings.DOMAIN_NAME + '/checkout/stripe/success',
                cancel_url= settings.DOMAIN_NAME + '/checkout/stripe/cancel',
                automatic_tax={'enabled': True}
            )

    except Exception as e:
        print(str(e))
        return JsonResponse({}, status=400)

    return JsonResponse({"checkout_session_url":checkout_session.url}, status=303)

