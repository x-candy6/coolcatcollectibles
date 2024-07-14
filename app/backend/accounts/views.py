from django.http import JsonResponse
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
    session_token = RefreshToken()
    access_token = str(session_token.access_token)
    refresh_token = str(session_token)
    return JsonResponse({
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
    if not access_token:
        return JsonResponse({'error': 'No token found.'}, status=404)
    try:
        # Validate Token
        access_token = AccessToken(access_token)

        if access_token.is_expired: # Check if expired
            return JsonResponse({'error': 'Expired token.'}, status=401)

    except (TokenError) as e: # Invalid Token
        return JsonResponse({'error': f'TokenError'}, status=400)
    except (InvalidToken) as e: # Invalid Token
        return JsonResponse({'error': f'Invalid Token'}, status=400)


    # Token is valid
    return JsonResponse({'message': 'Token is valid.'}, status=200)

@csrf_exempt
def refresh_session_token(request):
    refresh_token = request.headers.get('session_refresh_token')

    if not refresh_token:
        return JsonResponse({'error': 'No refresh token found.'}, status=404)
    refresh = RefreshToken(refresh_token)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return JsonResponse({
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
