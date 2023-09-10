from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def dashboard(request):
    products = models.Product.objects.all()
    products_per_row = []
    row = []
    
    for product in products:
        row.append(product)
        if len(row)==6:
            products_per_row.append(row)
            row = []
    if row:
        products_per_row.append(row)
    
    context = {
        'products_per_row': products_per_row,
    }

    return render(request, 'Product/dashboard.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    context = {
        'product':product,
    }

    if request.method == "POST":
        user_cart = models.Cart.objects.get(id=request.user.id)

        cart_item, created = models.CartItem.objects.get_or_create(cart=user_cart, product=product)

        if created:
            cart_item.quantity = 1
        else:
            cart_item.quantity +=1

        cart_item.save()

        #print(user_cart.cartitem_set.all())

        context = {
            'product':product,
            'sysMsg': "You have successfully added a product to your cart."
        }

        return render(request, "Product/detail.html", context)


    return render(request, "Product/detail.html", context)
    


def cart(request, user_id):
    user_cart = models.Cart.objects.get(id=request.user)
    print(user_cart.cartItems.all())
    context = {
        'cart_items':user_cart.cartitem_set.all(),
    }
    return render(request, "Product/cart.html", context)