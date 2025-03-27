from django.shortcuts import render
from .models import Food
# Create your views here.


def index(request):
    """View function for home page of site."""

    foods = Food.objects.all()


    return render(request, 'ccapp/index.html', {'foods': foods})