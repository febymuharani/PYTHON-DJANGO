from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


# Create your views here.

@permission_required('blog.can_edit')
def UpdateView(request):
    context = {
        'page_title' : 'Update Artikel'
    }
    return render(request, 'blog/edit.html', context)



#@permission_required('blog.add_artikel')
#@permission_required('blog.add_artikel',login_url='/admin/')
@permission_required('blog.add_artikel',login_url=None, raise_exception=True)
def AddView(request):
    context = {
        'page_title' : 'Add Artikel'
    }
    return render(request, 'blog/add.html', context)


def IndexViews(request):
    print(request.user.get_all_permissions())
    context = {
        'page_title' : 'Blog'
    }
    return render(request, 'blog/index.html', context)