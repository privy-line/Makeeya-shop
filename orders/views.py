from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['today_price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return redirect('cart:payment', order.id)    
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})