from django.shortcuts import render

# Create your views here.restaurant
from . models import restaurant


def rest(request,rt):
	rt=restaurant.objects.filter(name=rt)[0]
	return render(request,"products/restaurant.html",{'restaurant':rt})

