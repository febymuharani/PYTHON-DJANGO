from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'blog',
        'kontributor':'fadil'
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul':'cerita',
        'kontributor':'kanza'
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul':'news',
        'kontributor':'rifki'
    }
    return render(request, 'blog/index.html', context)
    