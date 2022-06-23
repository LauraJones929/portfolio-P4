from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """
    A function that renders the bag's contents
    """
    return render(request, 'bag/bag.html')