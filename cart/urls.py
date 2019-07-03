from django.conf.urls import url
from . import views

app_name = 'cart' 


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<item_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<item_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^buyer_registration/',views.buyer_registration,name='buyer_registration'),
    url(r'^buyer_login/',views.buyer_login,name='buyer_login'),
    url(r'^payment/(\d+)$',views.payment,name='payment')
]