from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """
    A function to show gym sessions and memberships
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)