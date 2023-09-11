import stripe
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms
# Create your views here.


def dash(request):
    products = models.Product.objects.all()

    pub_options = models.Product.objects.values_list(
        'publisher_name', flat=True).distinct()
    year_options = models.Product.objects.values_list(
        'year', flat=True).distinct()
    series_options = models.Product.objects.values_list(
        'series_name', flat=True).distinct()

    filter_form = forms.ProductFilterForm(
        request.POST or None, pub_options=pub_options, year_options=year_options, series_options=series_options)

    if request.method == 'POST':
        print(request.POST)
        filter_form = forms.ProductFilterForm(
            request.POST or None, pub_options=pub_options, year_options=year_options, series_options=series_options)
        if filter_form.is_valid():
            selected_publisher = filter_form.cleaned_data.get('publisher_list')
            selected_years = filter_form.cleaned_data.get('year_list')
            # selected_years = filter_form.cleaned_data.get(
            #   int(year) for year in filter_form.cleaned_data.get('year_list'))
            selected_series = filter_form.cleaned_data.get('series_list')
            print(selected_publisher)
            print(selected_series)
            print(selected_years)
            # Filter products based on the form input
        if selected_publisher:
            products = products.filter(publisher_name__in=selected_publisher)
        if selected_years:
            products = products.filter(year__in=selected_years)
        if selected_series:
            products = products.filter(series_name__in=selected_series)

        # Additional cases
        if selected_publisher and selected_years:
            # Filter by publisher and years
            products = products.filter(
                publisher_name__in=selected_publisher,
                year__in=selected_years
            )
        if selected_publisher and selected_series:
            # Filter by publisher and series
            products = products.filter(
                publisher_name__in=selected_publisher,
                series_name__in=selected_series
            )
        if selected_years and selected_series:
            # Filter by years and series
            products = products.filter(
                year__in=selected_years,
                series_name__in=selected_series
            )

        # Additional cases for all three filters combined
        if selected_publisher and selected_years and selected_series:
            # Filter by publisher, years, and series
            products = products.filter(
                publisher_name__in=selected_publisher,
                year__in=selected_years,
                series_name__in=selected_series
            )

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
        'filter_form': filter_form,
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
