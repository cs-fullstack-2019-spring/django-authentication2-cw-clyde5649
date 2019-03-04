from django.contrib import admin
from . import views
from django.urls import path, include


# path for the user to get the where they need to
urlpatterns = [
    path('',views.index,name ='index')


]