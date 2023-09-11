from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.backends import ModelBackend
import requests
from . import forms
from . import models
from Product import models as ProductModels

# Create your views here.


def home(request):
    return render(request, 'User/home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password,
                            backend='django.contrib.auth.backends.ModelBackend')

        if user is not None:
            login(request, user)
            return redirect('User:home')
        else:
            retVals = {
                'username': username,
                'password': password,
                'error': True,
                'modalTitle': 'Invalid Login',
                'modalText': 'The username and password combination that you entered was invalid. Please try again. If this continues, please contact support by clicking the "Contact Us" link at the bottom of the page.',
                'modalBtnText': "Close",
                'modalImmediate': True
            }
            return render(request, 'User/login.html', retVals)

    context = {}
    return render(request, 'User/login.html')


def logoutPage(request):
    # The following also clears session data
    logout(request)
    return redirect('home')


def registrationPage(request):
    # print(request.session.session_key)
    # print(request.session['visitorIP'])
    user_form = forms.SignUpForm()
    if request.method == 'POST':
        # Prepare the session and the forms.
        user_form = forms.SignUpForm(request.POST)
        # Check for Validation errors and send them back to the page
        if not user_form.is_valid():
            print(user_form.errors)
            return render(request, 'User/signup.html', {'user_form': user_form, 'feedback': "Error", 'error': user_form.errors})
        else:
            # Save the user, the account, and log in the new user
            user = user_form.save(request)

            user.username = request.POST['username']
            user.email = request.POST['email']
            user.password = request.POST['password1']

            if user is not None:

                authenticate(request, username=user.username, password=user.password,
                             backend='django.contrib.auth.backends.ModelBackend')
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')

                profile = models.Profile(id=user)
                profile.save()

                cart = ProductModels.Cart(id=user)
                cart.save()

                return render(request, 'User/home.html')

            else:
                # There was an error authenticating the newly registered user.
                return render(request, "User/invalidLogin.html")
    # If just a GET request, then send them the html.
    return render(request, 'User/signup.html', {'user_form': user_form})


def profile(request):
    profile_form = forms.ProfileForm()
    context = {
        'profile_form': profile_form,

    }
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST)

        if not profile_form.is_valid():
            print(profile_form.errors)
            return render(request, "User/profile.html", context)
        else:
            profile_form.save(request)
            return render(request, "User/profile.html", context)

    return render(request, "User/profile.html", context)
