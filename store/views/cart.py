from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..models.products import Products

# Create your views here.

class Cart(View):

    def get(self,request):

        cart_ids=list(request.session.get('cart').keys())
        cart_items=Products.get_products_by_id(cart_ids)
        return render(request,"cart.html",{'cart_items':cart_items})
    

    # cart_data=request.session.class ModelCreateView(CreateView):
    #         model = Model
    #         template_name = ".html"