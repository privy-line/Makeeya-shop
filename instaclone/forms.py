from django import forms 
from django.contrib.auth.models import User
# from .models import Profile,Buyer,Request

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Item, User, Profile ,Request
from django.forms.utils import ValidationError




class ImageForm(forms.ModelForm):  
    class Meta:
        model = Item
        exclude = ['post_date', 'profile']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

 


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
class EditItemForm(forms.ModelForm):  
    class Meta:
        model = Item
        exclude = ['post_date', 'profile','item_name','item_picture','expiry_date','stock','original_price','today_price']
    
