from django.shortcuts import render

# Create your views here.restaurant
from . models import restaurant,food
from . forms import food_form ,rest_form
from . serializers import food_S,rest_S 
from django.http import HttpResponse,HttpResponseRedirect

def rest(request,rt):
	rt=restaurant.objects.filter(name=rt)[0]
	return render(request,"products/restaurant.html",{'restaurant':rt})

def add_food(request):
	f=food_form()
	if request.method=="POST":
		print(request.POST)
		item=request.POST
		serializer = food_S(data=item)
		if (serializer.is_valid()):
			serializer.save()
		else:
			print(serializer.errors)
			return HttpResponse("<h1>opps somthing went wrong<h1/>")
			
	
	return render(request,"products/add_rest.html",{"f":f})

def edit_food(request):
	pass

	return

def add_rest(request):
	f=rest_form()
	if request.method=="POST":
		print(request.POST)
		item=request.POST
		serializer = rest_S(data=item)
		if (serializer.is_valid()):
			serializer.save()
			return HttpResponseRedirect('')

		else:
			print(serializer.errors)
			return HttpResponse("<h1>opps somthing went wrong<h1/>")
			
	
	return render(request,"products/add_rest.html",{"f":f})
	

# def edit_food(request):
# 	return