from django import forms
from .models import Buyer


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class BuyerForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields = "__all__"

class BuyerLoginForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields = ['email','password']