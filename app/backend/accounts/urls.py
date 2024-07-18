from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.registerUser, name='register'),
    path('api/login/', views.loginUser, name='login'),
    path('api/logout/', views.logoutUser, name='logout'),
    path('api/user/<str:token>/', views.getUserData, name='getUserData'),

    path('api/session/validate_token/', views.validate_session_token, name='validate_session_token'),
    path('api/session/refresh_token/', views.refresh_session_token, name='refresh_session_token'),
    path('api/session/issue_token/', views.issue_session_token, name='issue_session_token'),

    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('api/cart/update/', views.update_cart, name='update_cart'),
    path('api/cart/get/', views.get_cart, name='get_cart'),

]
