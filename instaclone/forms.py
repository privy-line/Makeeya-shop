from django import forms 
from django.contrib.auth.models import User
# from .models import Profile,Buyer,Request

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Item, User, Profile,Buyer,Request
from django.forms.utils import ValidationError


class BuyerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
        return user


class SellerSignUpForm(UserCreationForm):    
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)        
        return user


class ImageForm(forms.ModelForm):  
    class Meta:
        model = Item
        exclude = ['post_date', 'profile']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

 
class BuyerForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields = "__all__"

class BuyerLoginForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields = ['email','password']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
