from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .form import CustomerRegistrationForm
# Create your views here.


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        cloths = {'cloth':[topwears,bottomwears]}

        return render(request, 'app/home.html', {'mobiles': mobiles, 'loptops': laptops,'dress':[topwears,bottomwears]})

# def product_detail(request):
#     return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Samsung' or data == 'Nokia':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request,data = None):
    if data == None :
        laptops = Product.objects.filter(category='L')
    elif data =='Dell' or data=='HP':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discounted_price__lt=30000)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discounted_price__gt=30000)
    return render(request,'app/laptop.html',{'laptops':laptops})


def bottomwear(request,data=None):
    if data== None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'ZUVINO' or data == 'Generic':
        bottomwears = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=400)
    elif data == 'above':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=400)
    return render(request,'app/bottomwear.html',{'bottomwears':bottomwears})

def topwear(request,data=None):
    if data== None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'DressBerry' or data == 'Generic':
        topwears = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=400)
    elif data == 'above':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=400)
    return render(request,'app/topwear.html',{'topwears':topwears})
def login(request):
    return render(request, 'app/login.html')


# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request)
        if form.is_valid():
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

def checkout(request):
    return render(request, 'app/checkout.html')
