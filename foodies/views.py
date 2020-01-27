from django.shortcuts import render
from product.models import restaurant 
def home(request):
	res=restaurant.objects.all()
	return render(request,"home.html",{"res":res})
