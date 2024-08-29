from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'Title' : 'Blog',
        'Heading' : 'INI PADA HALAMAN BLOG',
        'Categori' : 'All',
        'Posts' : posts,
    }


    return render(request, 'index.html', context)


def jurnal(request):
    posts = Post.objects.filter(kategori='jurnal')
    context = {
        'Title' : 'Blog',
        'Heading' : 'JURNAL',
        'Categori' : 'jurnal',
        'Posts' : posts,
    }


    return render(request, 'index.html', context)



def cerpen(request):
    posts = Post.objects.filter(kategori='cerpen')
    context = {
        'Title' : 'Blog',
        'Heading' : 'CERITA PENDEK',
        'Categori' : 'cerpen',
        'Posts' : posts,
    }


    return render(request, 'index.html', context)

def berita(request):
    posts = Post.objects.filter(kategori='berita')
    context = {
        'Title' : 'Blog',
        'Heading' : 'BERITA TERKINI!!',
        'Categori' : 'berita',
        'Posts' : posts,
    }


    return render(request, 'index.html', context)