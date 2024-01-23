from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Products
# Create your views here.

def index(request):

    products=Products.get_all_products()
    print(products)

    # return HttpResponse("hello world")
    data={'products':products}
    return render(request,"index.html",data)

