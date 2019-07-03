from django import forms
from .models import Order,Payment


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phonenumber']