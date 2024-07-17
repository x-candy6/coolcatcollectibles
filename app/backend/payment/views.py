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

@api_view(['GET'])
@csrf_exempt
def validate_session_token(request):

    # Get Token
    access_token = request.headers.get('session-access-token')
    print(access_token)
    # No Token Found
    if not access_token:
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
