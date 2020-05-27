from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import ALLPRODUCT

# Register your models here.
class ALLPRODUCT_ADMIN(ModelAdmin):
    search_fields = ['title']
admin.site.register(ALLPRODUCT,ALLPRODUCT_ADMIN)

