from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.views.decorators.cache import cache_control
from .models import Product, Cart, Wishlist
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "marketplace/register.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return HttpResponse("Passwords must match")
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return HttpResponse("Username Taken")
        
        return HttpResponseRedirect(reverse('marketplace:login'))

def login_view(request):
    if request.method == 'GET':
        return render(request, "marketplace/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("marketplace:index"))
        else:
            return HttpResponse("ERROR")

# @cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("marketplace:index"))

# @login_required(login_url='/login')
# @cache_control(no_cache=True, must_revalidate=True)
def index(request):
    products = list(Product.objects.all())
    return render(request, "marketplace/homepage.html", {
        "products":products
    })


def products(request, prod_id):
    if request.method == 'GET':
        product_info = list(Product.objects.filter(id=prod_id))
        return render(request, "marketplace/product.html", {"products": product_info})
    if request.method == 'POST':
        prod_id = request.POST.get('prods_id')
        action = request.POST.get('action')
        prod_check = Cart.objects.filter(prod_id=prod_id).filter(username=request.user.username)
        if action == "0":
            prod_obj = Product.objects.get(id=prod_id)
            if len(prod_check) == 0:
                cart = Cart(prod_id=prod_obj, username = request.user.username)
                cart.save()
                messages.success(request, 'Added to Cart Successfully')
                return HttpResponseRedirect(reverse('marketplace:product', kwargs={'prod_id': prod_id}))
            else:
                messages.error(request, 'Item already exists in cart')
                return HttpResponseRedirect(reverse('marketplace:product', kwargs={'prod_id': prod_id}))
        else:
            cart_del = Cart.objects.get(prod_id=prod_id, username=request.user.username)
            cart_del.delete()
            messages.success(request, 'Removed from cart successfully')
            return HttpResponseRedirect(reverse('marketplace:cart'))
            

@login_required(login_url='/login')
def cart(request):
    if request.method == 'GET':
        user = request.user.username
        user_cart = list(Cart.objects.filter(username=user))
        return render(request, "marketplace/cart.html", {
            "products": user_cart
        })

@login_required(login_url='/login')
def checkout(request):
    if request.method == 'GET':
        user = request.user.username
        user_cart = list(Cart.objects.filter(username=user))
        total = 0
        for i in range(len(user_cart)):
            total += user_cart[i].prod_id.price
        return render(request, "marketplace/checkout.html", {
            "products": user_cart,
            "totals": total
        })


def wishlist(request):
    if request.method == 'GET':
        user = request.user.username
        user_wish = list(Wishlist.objects.filter(username=user))
        return render(request, "marketplace/wishlist.html", {
            "products": user_wish
        })
    else:
        id = request.POST.get('prods_id')
        action = request.POST.get('action')
        if action == "1":
            wish_del = Wishlist.objects.get(prod_id=id, username=request.user.username)
            wish_del.delete()
            messages.success(request, 'Removed from wishlist successfully')
            return HttpResponseRedirect(reverse('marketplace:product', kwargs={'prod_id': id}))
        else:
            prod_check = Wishlist.objects.filter(prod_id=id).filter(username=request.user.username)
            if len(prod_check) == 0:
                prod_obj = Product.objects.get(id=id)
                wish = Wishlist(prod_id=prod_obj, username=request.user.username )
                wish.save()
                messages.success(request, 'Added to Wishlist Successfully')
                return HttpResponseRedirect(reverse('marketplace:product', kwargs={'prod_id': id}))
            else:
                messages.error(request, 'Item already exists in wishlist')
                return HttpResponseRedirect(reverse('marketplace:product', kwargs={'prod_id': id}))