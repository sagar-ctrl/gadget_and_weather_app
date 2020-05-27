from django.db import models

# Create your models here.
class ALLPRODUCT(models.Model):
    image=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    gadget_link=models.CharField(max_length=200)
    def __str__(self):
        return self.title
