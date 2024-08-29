from django.shortcuts import render

def index(request):
    context ={
        'judul':'kelas terbuka',
        'kontributor':'feby'
    }
    return render(request,'index.html', context)