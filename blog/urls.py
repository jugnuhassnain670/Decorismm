from django.urls import path
from . import views


urlpatterns = [
    path('', views.Blogs, name='blog'),
    path('blogdetail/<int:pk>', views.BlogsDetail, name='blog_detail'),
]
