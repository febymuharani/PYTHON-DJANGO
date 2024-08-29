from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'kelas terbuka',
        'subjudul':'Blog',
        'nav':[
            ['/','Home'],
            ['/blog/cerita','Cerita'],
            ['/blog/news','News']
        ]
    }
    return render(request,'index.html', context)