from cart.forms import CartAddProductForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,HttpResponseRedirect,HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Item,Profile,Request,Category,User
from cart.cart import Cart
# from oders.models import Oder
from django.contrib.auth.models import User
from .forms import ImageForm, ProfileForm ,RequestForm
from .email import send_notification_email
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
import datetime as dt

from django.views.generic import CreateView
 
# from django.shortcuts import render, get_object_or_404
 
# from cart.forms import CartAddProductForm
from django.views.generic import TemplateView


# class SignUpView(TemplateView):
#     template_name = 'registration/signup.html'

# class SellerSignUpView(CreateView):
#     model = User
#     form_class = SellerSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'seller'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('profile')


# class BuyerSignUpView(CreateView):
#     model = User
#     form_class = BuyerSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'buyer'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('cart:cart_detail')

def home(request):
    title = 'Home'
    items = Item.objects.all()

    return render(request, 'home.html', {'title':title, 'items':items})

def product_list(request,category_slug=None): 
    category = None
    categories = Category.objects.all()
    today = dt.date.today()
    products = Item.objects.filter(expiry_date=today)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Item.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def detail(request, item_id):
    item = Item.objects.filter(id=item_id)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'detail.html',{"item":item,"cart_product_form":cart_product_form,"item_id":item_id},item_id)


@login_required(login_url='/accounts/login/')
def profile (request):
    current_user=request.user 
          
    profile_details =  Profile.objects.get(user=current_user.id)    
    print(profile_details.business_logo)
    items=Item.get_profile_items(profile_details.user_id)
  

    return render(request,'profile.html',{'profile':profile,'profile_details':profile_details,'items':items})


@login_required(login_url='/accounts/login')
def create_item(request):
    current_user=request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = current_user           
            upload.save()
            return redirect('profile')
    else:
        form = ImageForm()
    
    return render(request, 'upload.html', {'form':form})


@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile')
            print(edit)
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html', {'form':form})
   
 

def comments(request,id):
        current_user = request.user
        
        post = Image.objects.get(id=id)
        comments = Comments.objects.filter(image=post)
        # print(comments)
        if request.method == 'POST':
                form = CommentsForm(request.POST,request.FILES)
                if form.is_valid():
                        comment = form.cleaned_data['comment']
                        new_comment = Comments(comment = comment,user =current_user,image=post)
                        new_comment.save() 

                        return redirect('home')                   
                
        else:
                form = CommentsForm()
        return render(request, 'comment.html', {"form":form,'post':post,'user':current_user,'comments':comments})




def view_comments(request):
    current_user=request.user   
    post = Image.objects.get(id=id)    
    image_comments= Comments.objects.filter(image=post)    
    return render(request,'home.html',{'image_comments':image_comments, 'post':post,'user':current_user})

 
def buyer_login(request):
    form = BuyerLoginForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            buyer=Buyer.objects.filter(email = form.cleaned_data['email']).first()
            if buyer.password==form.cleaned_data['password']:
                return redirect('home')
    return render(request,'buyer_login.html',{"form":form})

def buyer_registration(request):
   current_user = request.user
   if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.user = current_user
            buyer.save()
        return redirect('buyer_login')
   else:
        form = BuyerForm()
   return render(request, 'buyer_registration.html', {"form": form})


def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            request = form.save(commit=False)
            request.save()
            name = request.business_name
            email = request.business_email
            send_notification_email(name, email)           
            HttpResponseRedirect('home')
            return redirect('home')
  
    else:
        
        form =RequestForm()
 
    return render(request, 'request_form.html',{'form':form})


# @require_POST
# def cart_add(request, item_id):
#     cart = Cart(request)  # create a new cart object passing it the request object 
#     item = get_object_or_404(Item, id=item_id) 
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
#     return redirect('home')


# def cart_remove(request, item_id):
#     cart = Cart(request)
#     item = get_object_or_404(Item, id=item_id)
#     cart.remove(item)
#     return redirect('cart_detail',item_id)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart_detail.html', {'cart': cart})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    today = dt.date.today()
    products = Item.objects.filter(expiry_date=today)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Item.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request,'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Item, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

