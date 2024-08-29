from django.shortcuts import render

def index(request):
    context = {
        'tittle':'Kelas Terbuka',
        'subjudul':'Selamat Datang',
        'subheading':'Di Kelas Terbuka',
    }
    return render(request, 'index.html', context)