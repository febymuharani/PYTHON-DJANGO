from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    context = {
        'judul' : 'Home Blog',
        'content' : 'Ini Halaman Pada Blog',
        'Categories': categories,
        'Posts' : posts
    }
    return render(request,'blog/index.html', context)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput);
    categories = Post.objects.values('category').distinct();
    context = {
        'judul' : 'Home Blog',
        'content' : 'tampilkan berdasarkan kategori',
        'Categories': categories,
        'Posts' : posts
    }
    return render(request,'blog/kategori.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput);
    categories = Post.objects.values('category').distinct();
    context = {
        'judul' : 'Home Blog',
        'content' : 'Ini Halaman Pada Blog',
        'Categories': categories,
        'Posts' : posts
    }
    return render(request,'blog/detail.html', context)