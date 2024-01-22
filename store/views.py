from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.

def index(request):

    # return HttpResponse("hello world")
    data={}
    return render(request,"index.html",data)

