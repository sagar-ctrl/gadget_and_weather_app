from django.db import models

# Create your models here.
class weather(models.Model):
    city_name=models.CharField(max_length=200,default="kathmandu")
    time=models.CharField(max_length=100,default="unable to parse")
    city_link=models.CharField(max_length=300,default="/")
    climate=models.CharField(max_length=300,default="")
    image=models.CharField(max_length=200,default="")
    temp=models.CharField(max_length=25,default="")
    def __str__(self):
        return self.city_name
