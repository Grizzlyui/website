from django.shortcuts import render
from django.views.generic import (ListView, 
    DetailView, 
    CreateView
)
from django.http import  HttpResponse
from .models import Post


def home_view(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #queryset = posts.objects.order_by('-date_posted')
    ordering = ['-id']


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


class PostDetailView(DetailView):
    model = Post


def about_view(request):
    return render(request, "blog/about.html", {'title': 'About'})