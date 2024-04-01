from http.client import HTTPResponse

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *

# Create your views here.
class BaseView(View):
    context = {}
    context['categories'] = Category.objects.all()
    context['brands'] = Brand.objects.all()
    context['sales'] = Product.objects.filter(labels='sales')


class HomeView(BaseView):
    def get(self, request):
        self.context['sliders'] = Slider.objects.all()
        self.context['subcategories'] = SubCategory.objects.all()
        self.context['ads'] = Ads.objects.all()
        self.context['hots'] = Product.objects.filter(labels='hot')
        self.context['news'] = Product.objects.filter(labels='new')
        self.context['reviews'] = Reviews.objects.all()

        return render(request, 'index.html', self.context)


class Categories(BaseView):
    def get(self, request, slug):
        ids = Category.objects.get(slug=slug).id
        self.context['category_product'] = Product.objects.filter(category_id=ids)
        return render(request, 'category.html', self.context)


class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query')
        if not query:
            return redirect('/')
        self.context['search_products'] = Product.objects.filter(name__icontains = query)

        return render(request, 'search.html', self.context)

class DetailView(BaseView):
    def get(self, request, slug):
        self.context
        self.context['detail_product'] = Product.objects.filter(slug=slug)
        self.context['product_reviews'] = ProductReviews.objects.filter(slug=slug)
        return render(request, 'product-detail.html', self.context)


def review(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        reviews = request.POST['reviews']
        star = request.POST['star']
        slug = request.POST['slug']

        data = ProductReviews.objects.create(
            username = username,
            email = email,
            review = reviews,
            slug = slug,
            stars = star
        )
        data.save()
        return redirect(f'/product-detail/{{slug}}')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password=password
                )
                user.save()
                messages.success(request,"User created. Please log in!")
        else:
            messages.error(request,"Password does not match")
            return redirect('/signup')
    return render(request,'signup.html')

def logout_view(request):
    logout(request)

    return redirect('/')


class CartView(BaseView):
    def get(self, request):
        self.context
        self.context['cart_views'] = Cart.objects.filter(username=request.user.username, checkout=False)
        count = 0
        total_price = 0
        for i in Cart.objects.filter(username=request.user.username, checkout=False):
            x = Cart.objects.filter(username=request.user.username, checkout=False)[count].total
            total_price = total_price+ x
            count = count+ 1
        self.context['total_price'] = total_price
        return render(request, 'cart.html', self.context)

def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug,username = username,checkout = False).quantity
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug = slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        quantity = quantity+1
        total = original_price*quantity
        Cart.objects.filter(slug = slug,username = username).update(quantity = quantity,total = total)
        return redirect('/cart')
    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        data = Cart.objects.create(slug=slug,
                            username=username,
                            total=original_price,
                            product = Product.objects.filter(slug = slug)[0]
                            )
        data.save()
        return redirect('/cart')


def remove_product(request, slug):
    username = request.user.username
    quantity = Cart.objects.get(slug=slug, username=username).quantity
    price = Product.objects.get(slug=slug).price
    discounted_price = Product.objects.get(slug=slug).discounted_price
    if discounted_price > 0:
        original_price = discounted_price
    else:
        original_price = price
    if quantity > 1:
        quantity = quantity - 1
        total = original_price * quantity
        Cart.objects.filter(slug=slug, username=username, checkout=False).update(quantity=quantity, total=total)
    else:
        Cart.objects.filter(slug=slug, username=username, checkout=False).delete()
    return redirect('/cart')


def delete_cart(request, slug):
    username = request.user.username
    Cart.objects.filter(slug=slug, username=username,checkout=False).delete()
    return redirect('/cart')


class CheckoutView(BaseView):
    def get(self, request):
        self.context
        self.context['checkout_views'] = Cart.objects.filter(username=request.user.username, checkout=False)
        count = 0
        total_price = 0
        for i in Cart.objects.filter(username=request.user.username, checkout=False):
            x = Cart.objects.filter(username=request.user.username, checkout=False)[count].total
            total_price = total_price + x
            count = count + 1
        self.context['total_price'] = total_price
        return render(request, 'checkout.html', self.context)

def checkout(request):
    username = request.user.username
    Cart.objects.filter(username=username,checkout=False).update(checkout=True)
    return redirect('/cart')