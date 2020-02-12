from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=100)
    detail=models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to="static/product/food/images")
    price = models.CharField(max_length=10,default = 'Free')
    
   

    def __str__(self):
        return self.name
class restaurant(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ManyToManyField('food',blank=True)
    address=models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to="static/product/restaurant/images")
   
    
   

    def __str__(self):
        return self.name
