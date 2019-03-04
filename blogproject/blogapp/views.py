from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from django.contrib.auth.decorators import login_required



# Create your views here.


# connect my page and there path page

def index(request):
    return HttpResponse('call me')






