from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    """ Model representing a food item. """

    name = models.CharField(max_length=500)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


    def __str__(self):
        return self.name
    

class Consume(models.Model):
    """ Model representing a food item consumed by a user. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)