from django.contrib import admin
from django.urls import path, include

from searcheverything import views

urlpatterns = [
    path('',views.indexes,name="index"),
    # path('gadgets/<int:pk>/',views.ProductDetail.as_view(),name="detail")
    path('gadgets/<int:pk>/',views.detailView,name="detail")
]
