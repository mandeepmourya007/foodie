from  rest_framework import viewsets
from . import models
from . import serializers


class foodViewset(viewsets.ModelViewSet):
	"""docstring for foodViewset"""
	queryset=models.food.objects.all()
	serializer_class= serializers.food_S
	