from django.urls import path
from . import views

urlpatterns = [
    # path('api/user/<str:token>/', views.getUserData, name='getUserData'),
    path('api/payments/stripe_checkout/', views.stripe_checkout, name='stripe_checkout'),

]
