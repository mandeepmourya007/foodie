from  rest_framwork import viewsets
from . import models
from . import serializers


class foodViewset(viewsets.ModelViewset):
	"""docstring for foodViewset"""
	q=models.food.objects.all()
	sc= serializers.food_S
	