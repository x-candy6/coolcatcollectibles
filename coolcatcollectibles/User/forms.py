from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models




class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        model.is_staff = False
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

class AddressForm(forms.Form):
    street = forms.CharField(max_length=100, label='Street Address')
    city = forms.CharField(max_length=50, label='City')
    state = forms.CharField(max_length=50, label='State')
    zip_code = forms.CharField(max_length=10, label='ZIP Code')


class SignUpForm(SignupForm):
    username = forms.CharField(max_length=32, label='username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

#    def save(self, request, user):
#        # Ensure you call the parent class's save.
#        # .save() returns a User object.
#        user.first_name = self.cleaned_data['first_name']
#        user.last_name = self.cleaned_data['last_name']
#        user.username = self.cleaned_data['username']
#        user.password = self.cleaned_data['password1']
#        user = super(SignUpForm, self)
#        user.save(request)
#
#        # Add your own processing here.
#
#        # You must return the original result.
#        return user
#
#    class Meta:
#        model = User
#        model.is_staff = False
#        fields = ['username', 'first_name', 'last_name',
#                  'email', 'password1', 'password2']