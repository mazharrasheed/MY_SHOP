from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from ..models.category import Category
from ..models.customer import Customer
from ..models.products import Products


class Index(View):

   def get(self,request):

      # request.session.get('cart').clear()
      products=None
      categories=Category.get_all_category()
      categoryID=(request.GET.get('category'))
      if categoryID:
         products=Products.get_all_produts_by_categoryid(categoryID)
      else:
            products=Products.get_all_produts()
      global data
      data={'products':products,'categories':categories}
      # print(request.session.get('email'))
      return render(request,"index.html",data)    

   def post(self,request):
      productid=request.POST.get('productid')
      cart=request.session.get('cart')
      if cart :
         qty=cart.get(productid)
         if qty:
            cart[productid]=qty+1
         else:
            cart[productid]=1
      else:
         cart={}
         cart[productid]=1
      request.session['cart']=cart
      print(productid,cart)
      return redirect('homepage')
   