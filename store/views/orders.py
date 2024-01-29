
from django.shortcuts import render
# from django.utils.decorators import method_decorator
from django.views import View

from ..models.orders import Orders

# from store.middlewares.auth import auth_middleware


# Create your views here.

class Order(View):

    # @method_decorator(auth_middleware)
    def get(self,request):
        customer=request.session.get('customer_id')
        orders=Orders.get_order_by_custid(customer)
        data={'orders':orders}
        return render(request,'orders.html',data)