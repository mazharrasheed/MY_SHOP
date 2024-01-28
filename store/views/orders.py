
from django.shortcuts import render
from django.views import View

from ..models.orders import Orders

# Create your views here.

class Order(View):

    def get(self,request):
        customer=request.session.get('customer_id')
        order=Orders.get_order_by_custid(customer)
        data={'order':order,}
        return render(request,'orders.html',data)