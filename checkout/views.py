from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment.")
        return redirect(reverse,('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LFkmUL6ySxgcCCj8VyuNDDNsMs8IU8RoeS4Z8BHT1VMUxhFTaeuX1aodgcyT4qFX4xZKpGLueE29qDjgDeYyr3g009SrG1Nma',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
