from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import url,include

app_name="product"
urlpatterns =[
	
#	path("edit_food",views.edit_food,name="edit_food"),
#	path("add_food",views.add_food,name="add_food"),
#	path("add_rest",views.add_rest,name="add_rest"),

	path("<str:rt>",views.rest),
    
]
