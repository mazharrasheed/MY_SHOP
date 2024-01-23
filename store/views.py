from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Category, Products

# Create your views here.

def index(request):

    products=Products.get_all_products()
    categories=Category.get_all_products()
    # return HttpResponse("hello world")
    data={'products':products,'categories':categories}
    return render(request,"index.html",data)

def show():
    pass