from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title'] #내용 채우기
    blog.body = request.GET['body'] #내용 채우기
    blog.pub_date = timezone.datetime.now() #내용 채우기
    blog.save()

    #새로운 글 url 주소로 이동
    return redirect('/blog/'+str(blog.id))

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'edit.html',{'blog':blog})

def update(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title'] #내용 채우기
    blog.body = request.GET['body'] #내용 채우기
    blog.pub_date = timezone.datetime.now() #내용 채우기
    blog.save()

    #새로운 글 url 주소로 이동
    return redirect('/blog/'+str(blog.id))

def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('home')