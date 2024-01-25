from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..models.category import Category
from ..models.customer import Customer
from ..models.products import Products

# Create your views here.

class Login(View):

    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        data={}
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
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
        
