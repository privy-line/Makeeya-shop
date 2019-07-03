from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns=[
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'^cart_detail/$', views.cart_detail, name='cart_detail'),
    url(r'^$',views.home,name='home'),  
    url(r'^upload/$', views.create_item, name='create_item'),
    url(r'^edit_profile',views.edit_profile, name='edit_profile'),
    url(r'^profile', views.profile, name='profile'), 
    url(r'^comments/(\d+)',views.comments,name="comments"),
 
    url(r'^request/$', views.post_request, name='post_request'),
    url(r'^product_list$', views.product_list, name='product_list'),
   
   
    url(r'^(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)