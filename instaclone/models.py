from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User  
from tinymce.models import HTMLField
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.conf import settings
from decimal import Decimal


 

 

 

class Profile(models.Model):
    business_logo = models.ImageField(upload_to='profile/',blank=True)
    business_description = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)


    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile




class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('instaclone:product_list_by_category', args=[self.slug])


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 50)     
    profile = models.ForeignKey(User,on_delete=models.CASCADE)    
    upload_date = models.DateTimeField(auto_now_add=True)
    item_picture = models.ImageField(upload_to='profile')
    expiry_date = models.DateTimeField(auto_now_add=False)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    original_price = models.IntegerField()
    today_price = models.IntegerField()

    class Meta:
        ordering = ('upload_date',)
        index_together=(('id','profile'),)

    def save_image(self):
        self.save()
    
    @classmethod
    def update_price(cls, update):
        pass
    
    @classmethod
    def get_item_by_id(cls):
        item = Item.objects.filter(id).first()
        return item
    
    @classmethod
    def get_profile_items(cls, profile):
        items = Item.objects.filter(profile__pk = profile)
        return items
    
    @classmethod
    def get_all_items(cls):
        items = Item.objects.all()
        return items
        
    def get_absolute_url(self):
        return reverse('product_detail' , args=[self.id])

 



class Request(models.Model):
    business_name = models.CharField(max_length =100)
    business_identification_number = models.CharField(max_length =100)
    prefered_username = models.CharField(max_length =100)
    business_phone_number = models.IntegerField ()
    business_email = models.EmailField()
    Business_address = models.CharField(max_length =100) 

    def __str__(self):
            return self.name

    def save_request(self):
            self.save()
        
    
# class Category(models.Model):
#     name = models.CharField(max_length=150, db_index=True)
#     slug = models.SlugField(max_length=150, unique=True ,db_index=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name', )
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('product_list_by_category', args=[self.slug])