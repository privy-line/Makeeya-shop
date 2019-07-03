from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from instaclone.models import Item
from .models import Buyer
from .cart import Cart
# from orders.models import Oder,OderItem
from .forms import CartAddProductForm,BuyerLoginForm,BuyerForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from orders.models import OrderItem, Order, Payment
from orders.forms import OrderCreateForm,PaymentForm
import random
import requests 

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
     
    return render(request, 'cart/detail.html', {'cart': cart})

def buyer_login(request):
    form = BuyerLoginForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            buyer=Buyer.objects.filter(email = form.cleaned_data['email']).first()
            if buyer.password==form.cleaned_data['password']:
                return redirect('orders:order_create')
    return render(request,'cart/buyer_login.html',{"form":form})

def buyer_registration(request):
   current_user = request.user
   if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.user = current_user
            buyer.save()
        return redirect('cart:buyer_login')
   else:
        form = BuyerForm()
   return render(request, 'cart/buyer_registration.html', {"form": form})
   
   
   
def payment(request,id):
    current_user = request.user
    data = {}
    hashed = random.randint(0,1000000)
    order = Order.objects.filter(id=id).first()
    items = OrderItem.objects.filter(order = order).all()
    print(items)
    prices = 0
    for item in items:
        prices += item.price*item.quantity
    print(prices)
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            pay = form.save(commit=False)
            data['amount'] = str(prices)
            data['phonenumber'] = pay.phonenumber
            data['clienttime'] = '1556616823718'
            data['action'] = "deposit"
            data['appToken'] = "1f2e2951c7e2e355b443"
            data['hash'] = hashed
            pay.user = current_user

            print(data)
            pay.save()
            payload = data
            url = "https://uplus.rw/bridge/"
            requests.post(url, data=payload)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {"form": form,"order":order,"prices":prices})    





 