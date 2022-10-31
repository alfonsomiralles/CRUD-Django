from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.

def create(request):
    place = Place(name="Lugar 1", address= "Calle del mono")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)
