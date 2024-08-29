from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'tittle':'About',
        'heading':'About',
        'subheading':'Halaman Pada About'
    }
    return render(request, 'about/index.html', context)