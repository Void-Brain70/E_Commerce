from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # slide = n//4 + ceil((n/4)-(n//4))
    # context ={
    #     'products': products,
    #     'slideNumber': slide,
    #     'range':(1,slide)  
    # }
    # l = [ [products,range(1,slide),slide],
    #       [products,range(1,slide),slide]
    #     ]
    # context ={
    #     'l':l
    # }  
    l = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        products = Product.objects.filter(category=cat)
        n = len(products)
        slide = n // 4 + ceil((n / 4) - (n // 4))
        l.append([products, range(1, slide), slide])
    context ={
         'l': l
        }      
    return render(request,"eshop/index.html",context)

def about(request):
    return render(request,"eshop/about.html")

def contact(request):
    return render(request,"eshop/contact.html")  

def tracker(request):
    return render(request,"eshop/tracker.html")

def search(request):
    return render(request,"eshop/search.html")

def productView(request):
    return render(request,"eshop/productView.html")

def checkout(request):
    return render(request,"eshop/checkout.html")                      
