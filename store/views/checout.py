from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..models.customer import Customer
from ..models.orders import Orders
from ..models.products import Products

# Create your views here.

class Cheout(View):

    def post(self,request):
        adress=request.POST.get('adress')
        phone=request.POST.get('phone')
        customer_id=request.session.get('customer_id')
        if not customer_id:
            return redirect("login")
        else:
            cart=request.session.get('cart')
            products=Products.get_products_by_id(list(cart.keys()))
            for product in products:
                order=Orders(
                    customer=Customer(id=customer_id),
                    product=Products(id=product.id),
                    qty=cart.get(str(product.id)),
                    price=product.pro_price,
                    adress=adress,
                    phone=phone, 
                )
                order.place_order()
            request.session['cart']={}
            return redirect("showcart")


