from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Vendor
from product.models import Product,Category
from django.utils.text import slugify
from .forms import ProductForm,ProductImageForm,BlogForm,SignUpForm

def become_vendor(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            vendor=Vendor.objects.create(name=user.username, created_by=user)
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request, 'become_vendor.html', {'form':form})

@login_required
def vendor_admin(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    orders = vendor.orders.all()
    
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'vendor_admin.html', {'vendor': vendor, 'products': products, 'orders': orders})

@login_required
def myCategory(request):
    vendor=request.user.vendor
    categorys=vendor.category.products.all()

    return render(request, 'myCategory.html', {'vendor': vendor, 'categorys': categorys})

@login_required
def myOrders(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    orders = vendor.orders.all()    
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'myOrders.html', {'vendor': vendor, 'products': products, 'orders': orders})

@login_required
def myProducts(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    return render(request, 'myProducts.html', {'vendor': vendor, 'products': products})

@login_required
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product=form.save(commit=False)
            product.vendor=request.user.vendor  
            product.slug= slugify(product.title)
            product.save()
            return redirect('add_product')
    else: 
        form=ProductForm()
    return render(request,'add_product.html', {'form':form})

@login_required
def myBlog(request):
    vendor=request.user.vendor
    blogs=vendor.blogs.all()
    return render(request, 'myBlog.html', {'vendor': vendor, 'blogs': blogs})

@login_required
def add_blogPost(request):
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blogpost=form.save(commit=False)
            blogpost.vendor=request.user.vendor  
            blogpost.slug= slugify(blogpost.title)
            blogpost.save()
            return redirect('vendor_admin')
    else: 
        form=BlogForm()
    return render(request,'add_blogPost.html', {'form':form,'vendor': vendor})

@login_required
def edit_blogPost(request,pk):
    vendor=request.user.vendor
    blogs=vendor.blogs.get(pk=pk)
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('myBlogs')
    else:
        form=BlogForm(instance=blogs)
    return render(request, 'edit_blogPost.html', {'form': form, 'blogs':blogs}) 

@login_required
def delete_blogPost(request,pk):
    vendor=request.user.vendor
    blogs=vendor.blogs.get(pk=pk)
    blogs.delete()
    return redirect('myBlogs')
    
@login_required
def edit_vendor(request):
    vendor = request.user.vendor
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        if name:
            vendor.created_by.email = email
            vendor.created_by.save()
            vendor.name = name
            vendor.save()
            return redirect('vendor_admin')    
    return render(request, 'edit_vendor.html', {'vendor': vendor})

@login_required
def edit_product(request, pk):
    vendor=request.user.vendor
    product=vendor.products.get(pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES, instance=product)
        image_form=ProductImageForm(request.POST, request.FILES)        
        if image_form.is_valid():
            productimage=image_form.save(commit=False)
            productimage.product=product
            productimage.save()           
            return redirect('vendor_admin')
        
        if form.is_valid():
            form.save()            
            return redirect('vendor_admin')
    else:
        form=ProductForm(instance=product)
        image_form=ProductImageForm()       
    return render(request, 'edit_product.html', {'form': form, 'product':product,'image_form':image_form})     

def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor.html', {'vendor': vendor})

