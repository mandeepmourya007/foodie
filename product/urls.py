from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import url,include

app_name="product"
urlpatterns =[
	
	path("<str:rt>",views.rest),
    
]
