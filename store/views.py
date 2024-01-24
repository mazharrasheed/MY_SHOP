from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models.category import Category
from .models.customer import Customer
from .models.products import Products

# Create your views here.

def index(request):

    products=None
    categories=Category.get_all_category()

    categoryID=(request.GET.get('category'))

    if categoryID:
       products=Products.get_all_produts_by_categoryid(categoryID)
    else:
         products=Products.get_all_produts()

    data={'products':products,'categories':categories}
    return render(request,"index.html",data)

def signup(request):

    if request.method=='GET':
        return render(request,"signup.html")
    else:

        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')

        error_message=None
        if (not firstname):
            error_message="First name requried"
        elif(len(firstname)<4):
            error_message="First name should be more then 4 character "

        if not error_message:
            customer=Customer(firstname=firstname,
                                lastname=lastname,
                                phone=phone,
                                email=email,
                                password=password                    
                                )
            customer.register()
            return redirect("/")

        else:

             return render(request,"signup.html",{'error':error_message})
