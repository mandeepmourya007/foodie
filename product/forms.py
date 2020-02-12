from . models import food,restaurant
from django import forms



class food_form(forms.ModelForm):
	class Meta:
		model=food
		fields='__all__'	
class rest_form(forms.ModelForm):
	class Meta:
		model=restaurant
		fields='__all__'	