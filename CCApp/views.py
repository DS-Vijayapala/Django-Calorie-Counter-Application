from django.shortcuts import render
from .models import Food, Consume
# Create your views here.


def index(request):
    """View function for home page of site."""

    if request.method == 'POST':

        user = request.user

        food_consumed = request.POST['food_consumed']

        consume = Food.objects.get(name=food_consumed)

        user = request.user

        consume = Consume(user=user, food_consumed=consume)

        consume.save()

        foods = Food.objects.all()

    else:

        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)

    context = {'foods': foods, 'consumed_food': consumed_food}

    return render(request, 'ccapp/index.html', context)
