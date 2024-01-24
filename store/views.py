from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models.category import Category
from .models.products import Products

# Create your views here.

def index(request):

    products=None
    categories=Category.get_all_category()
    categoryID=request.GET.get('category')
    
    if categoryID:
        products=Products.get_all_produts_by_categoryid(categoryID)
    else:
        products=Products.get_all_produts()
    # return HttpResponse("hello world")
    data={'products':products,'categories':categories}
    return render(request,"index.html",data)

def signup(request):

    if request.method=='GET':
        return render(request,"signup.html")
    else:
        return HttpResponse(request.POST.get("firstname"))

