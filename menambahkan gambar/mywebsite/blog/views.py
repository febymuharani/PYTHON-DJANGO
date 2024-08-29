from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Blog',
        'subjudul':'Ini Halaman Blog Pada Kelas Terbuka',
        'banner':'blog/img/banner_blog.png',
        'app_css':'blog/css/style.css',
    }
    return render(request, 'index.html', context)