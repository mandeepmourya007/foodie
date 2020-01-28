from rest_framework import serializers 
from . models import food,restaurant

class food_S(serializers.ModelSerializer):
	class Meta:
		model=food
		fields='__all__'
	#	field=["name","detail",'image',"price"]
