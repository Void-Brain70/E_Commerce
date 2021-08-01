from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
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
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"eshop/contact.html")  

def tracker(request):
    return render(request,"eshop/tracker.html")

def search(request):
    return render(request,"eshop/search.html")

def productView(request,id):
    products = Product.objects.filter(id=id)
    print(products)  
    return render(request,"eshop/productView.html",{'products':products[0]})

def checkout(request):
    return render(request,"eshop/checkout.html")                      
