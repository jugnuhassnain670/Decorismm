from .models import blogs
from django.shortcuts import render


def Blogs(request):
    posts = blogs.objects.all()

    return render(request, 'blog.html', {'posts': posts})

def BlogsDetail(request, pk):
    post = blogs.objects.get(pk=pk)

    return render(request, 'blogdetail.html', {'post': post})   
