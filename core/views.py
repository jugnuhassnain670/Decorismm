from django.shortcuts import render,redirect
from product.models import Product,Category
from blog.models import blogs
from .models import NewsLetter,ContactUs

def index(request):
    newest_products=Product.objects.all()[0:8]
    posts = blogs.objects.all()
    return render(request, 'index.html', {'newest_products': newest_products,'posts': posts})

def NewsLetters(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        news=NewsLetter(email=email)
        news.save()
        return redirect('home')
    return render(request, 'base.html')

def Contactus(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=ContactUs(name=name,email=email,message=message)
        contact.save()
        
    return render(request, 'contactUs.html')


