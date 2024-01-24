from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models.category import Category
from .models.customer import Customer
from .models.products import Products
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

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

def validateCustomer(customer,repassword):
    error_message=None
    if not customer.firstname:
        error_message="First name requried"
    elif len(customer.firstname)<4:
        error_message="First name should be more then 4 character"
    elif len(customer.phone)<10:
        error_message="Phone number must be 10 char long"
    elif len(customer.email)<5:
        error_message="Email must be 5 char long"
    elif len(customer.password)<8:
        error_message="Password must be 8 char long"
    elif customer.password!= repassword:
        error_message="Passsword not matched please enter again"
    elif customer.isExist():
        error_message="Email allready registerd"

    return error_message

def regisgterUser(request):
    data={}
    postData=request.POST
    firstname=postData.get('firstname')
    lastname=postData.get('lastname')
    phone=postData.get('phone')
    email=postData.get('email')
    password=postData.get('password')
    repassword=postData.get('repassword')
    values={'firstname':firstname,
        'lastname':lastname,
        'phone':phone,
        'email':email,}
    customer=Customer(firstname=firstname,
                    lastname=lastname,
                    phone=phone,
                    email=email,
                    password=password)
    error_message=None
    error_message=validateCustomer(customer,repassword)
    if not error_message:
        customer.password=make_password(customer.password)
        customer.register()
        return redirect("/")
    else:
        data={'error':error_message,'values':values}
        return render(request,"signup.html",data)

def signup(request):
    
    if request.method=='GET':
        return render(request,"signup.html")
    else:
        return regisgterUser(request)
    
class Login(View):
    def get(self,request):
        if request.method=='GET':
            return render(request,"login.html")
    def post(self,request):
            data={}
 
            email=request.POST.get('email')
            password=request.POST.get('password')
            customer=Customer.get_customer_by_email(email)
            print(customer)
            error_message=None
            if customer:
                flag=check_password(password,customer.password)
                if flag:
                    return redirect("/")
                else:
                    error_message="Email or Password invalid"
            else:
                error_message="Email or Password invalid"
            values={
            'email':email,}
            if error_message:
                data={'values':values,'error':error_message}
                return render(request,"login.html",data)
        

            
# def login(request):
        
#         data={}
#         if request.method=='GET':
#             return render(request,"login.html")
#         else:
#             email=request.POST.get('email')
#             password=request.POST.get('password')
#             customer=Customer.get_customer_by_email(email)
#             print(customer)
#             error_message=None
#             if customer:
#             flag=check_password(password,customer.password)
#             if flag:
#                 return redirect("/")
#             else:
#                 error_message="Email or Password invalid"
#             else:
#                 error_message="Email or Password invalid"
#             values={
#             'email':email,}
#             if error_message:
#                 data={'values':values,'error':error_message}
#                 return render(request,"login.html",data)
        
