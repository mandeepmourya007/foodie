from django.contrib import admin
from .  models import food,restaurant
# Register your models here.
admin.site.register(food)
admin.site.register(restaurant)
admin.site.site_header = "FOODIE"