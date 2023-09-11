import stripe
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.


def dashboard(request):
    products = models.Product.objects.all()
    products_per_row = []
    row = []

    for product in products:
        row.append(product)
        if len(row) == 6:
            products_per_row.append(row)
            row = []
    if row:
        products_per_row.append(row)

    context = {
        'products_per_row': products_per_row,
    }

    return render(request, 'Product/dashboard.html', context)


def dash(request):
    products = models.Product.objects.all()
    paginator = Paginator(products, 24)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Handle the case where the page number is not an integer
        page = paginator.page(1)  # Show the first page instead
    except EmptyPage:
        page = paginator.page(1)

    context = {
        'products_per_row': page,
    }

    return render(request, 'Product/dash.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    context = {
        'product': product,
    }

    if request.method == "POST":
        user_cart = models.Cart.objects.get(id=request.user.id)

        cart_item, created = models.CartItem.objects.get_or_create(
            cart=user_cart, product=product)

        if created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1

        cart_item.save()

        # print(user_cart.cartitem_set.all())

        context = {
            'product': product,
            'sysMsg': "You have successfully added a product to your cart."
        }

        return render(request, "Product/detail.html", context)

    return render(request, "Product/detail.html", context)


def cart(request, user_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    STRIPE_PUB_KEY = settings.STRIPE_PUBLISHABLE_KEY

    user_cart = models.Cart.objects.get(id=request.user)
    items = user_cart.cartitem_set.all()
    total = []
    for item in items:
        total.append(item.getTotal())
    total = int(sum(total) * 100)
    print(total)

    context = {
        'cart_items': user_cart.cartitem_set.all(),
        'STRIPE_PUBLISHABLE_KEY': STRIPE_PUB_KEY,
        'amount': total,
        'currency': 'usd',
        'data-zip-code': "true",
        'data-locale': "auto",
        "description": "",
    }

    if request.method == 'POST':
        token = request.POST['stripeToken']

        try:
            charge = stripe.Charge.create(
                amount=total,  # in cents
                currency='usd',
                source=token,
                description="Test Charge"

            )

        except stripe.error.CardError as e:
            print(e)

    return render(request, "Product/cart.html", context)
