from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..models.category import Category
from ..models.customer import Customer
from ..models.products import Products

# Create your views here.

class Signup(View):

    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        return self.regisgterUser(request)

    def validateCustomer(self,customer,repassword):
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

    def regisgterUser(self,request):
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
        error_message=self.validateCustomer(customer,repassword)
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect("/")
        else:
            data={'error':error_message,'values':values}
            return render(request,"signup.html",data)

    
    
