"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from myshop import settings
from store.views.cart import Cart
from store.views.checout import Cheout
from store.views.home import Index
from store.views.login import Login, logout
from store.views.signup import Signup

urlpatterns = [
    path('',            Index.as_view(),        name='homepage'),
    path('signup/',     Signup.as_view(),       name='signup'),
    path('login/',      Login.as_view(),        name='login'),
    path('logout/',     logout,                 name='logout'),
    path('showcart/',   Cart.as_view(),         name='showcart'),
    path('checkout/',   Cheout.as_view(),       name='checkout'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
