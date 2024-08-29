from django.shortcuts import render

def index(request):
    context = {
        'heading' : 'HOME',
        'content' : 'ini adalah home',
    }

    return render(request, 'index.html', context)