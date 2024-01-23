from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Category, Products

# Create your views here.

def index(request):

    products=None
    categories=Category.get_all_products()

    categoryID=(request.GET.get('category'))

    if categoryID:
       products=Products.get_all_products_by_categoryid(categoryID)
    else:
         products=Products.get_all_products()

 
 
    data={'products':products,'categories':categories}
    return render(request,"index.html",data)

def signup(request):

    data={}
    return render(request,"signup.html",data)