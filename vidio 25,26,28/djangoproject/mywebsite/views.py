from django.shortcuts import render


def index(request):
    context = {
        'judul' : 'Home Page',
        'content' : 'Ini Halaman Pada Page Awal'
    }
    return render(request, 'index.html', context)