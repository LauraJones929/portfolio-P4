from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A function to render home page
    """
    return render(request, 'home/index.html')
