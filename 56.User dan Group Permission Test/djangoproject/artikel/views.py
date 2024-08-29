from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
# Create your views here.

# CUSTOM CHECK
@user_passes_test(lambda user: user.username == 'otong')
def OtongView(request):
    return render(request, 'artikel/otong.html', {})



# SIMPLE DECORATOR CHECK
@user_passes_test(lambda user: Group.objects.get(name='penulis') in user.groups.all())
def ArtikelAddView2(request):
    context = {
        'page_title' : 'Tambah Artikel View'
    }
    return render(request, 'artikel/artikel_add.html', context)





# DECORATOR CHECK
def checkPenulis(user):
    test_group = Group.objects.get(name='penulis')
    user_group = user.groups.all()

    status = test_group in user_group
    print(status)
    return status

@user_passes_test(checkPenulis)
def ArtikelAddView(request):
    context = {
        'page_title' : 'Tambah Artikel View'
    }
    return render(request, 'artikel/artikel_add.html', context)


# INTERNAL CHECK 

def ArtikelIndexViews(request):
    context = {
        'page_title' : 'Artikel'
    }

    test_group = Group.objects.get(name='penulis')
    user_group = request.user.groups.all()


    template_name = None
    if test_group in user_group:
        #Logika untuk user dalam group
        template_name = 'artikel/index_penulis.html'
    else:
        #Logika untuk user di luar grup
        template_name = 'artikel/index_pembaca.html'

    return render(request, template_name, context)