from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/general/<str:token>/', views.getGeneralInventory, name='getGeneralInventory'),
    path('api/updateItem/', views.updateInventoryItem, name='updateInventoryItem'),
    path('api/search/<str:category>/<str:query>/', views.searchInventory, name='searchInventory'),

    re_path(r'^api/catalog/(?P<category>\w+)?/?(?P<query>.+)?/?$', views.getCatalog, name='getCatalog'),

    path('api/product/<str:itemID>/', views.getItem, name='getItem'),
]
