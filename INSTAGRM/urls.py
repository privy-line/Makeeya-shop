"""INSTAGRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views

from instaclone.views import SellerSignUpView, BuyerSignUpView,SignUpView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart',include('cart.urls')),
    url(r'^orders/',include('orders.urls')),
    url(r'',include('instaclone.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 

    url('^accounts/signup/$',SignUpView.as_view(), name='signup'),
    url('^accounts/signup/seller/$',SellerSignUpView.as_view(), name='seller_signup'),
    url('^accounts/signup/buyer/$',BuyerSignUpView.as_view(), name='buyer_signup'),

]
