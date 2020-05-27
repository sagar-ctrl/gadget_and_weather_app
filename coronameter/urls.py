from django.contrib import admin
from django.urls import path, include

from coronameter import views

urlpatterns = [

    path('',views.index,name="index"),
    path('weather_city/<int:pk>/',views.city_detail,name="detail")
]
