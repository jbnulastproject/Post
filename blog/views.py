from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from rest_framework import viewsets
from django.utils import timezone

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def post(request):
    return render(request,'blog/post.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))