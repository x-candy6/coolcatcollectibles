from django.urls import path

from . import views

app_name = "Product"
urlpatterns = [
    path("", views.dash, name="dash"),
    path("<int:user_id>", views.cart, name="cart"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
]
