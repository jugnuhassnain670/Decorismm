from django import views
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('become-vendor/',views.become_vendor,name='become_vendor'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('vendor-admin/',views.vendor_admin,name='vendor_admin'),
    path('add-product/',views.add_product,name='add_product'),
    path('myBlogs/', views.myBlog, name='myBlogs'),
    path('add-blogPost/',views.add_blogPost,name='add_blogPost'),
    path('edit-blogPost/<int:pk>/',views.edit_blogPost,name='edit_blogPost'),
    path('delete-blogPost/<int:pk>/',views.delete_blogPost,name='delete_blogPost'),
    path('myProducts/', views.myProducts, name='myProducts'),
    path('myCategory/', views.myCategory, name='myCategory'),
    path('myOrders/', views.myOrders, name='myOrders'),
]

