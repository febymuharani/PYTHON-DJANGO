from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# View method dengan internal permission checks
def index(request):
    context = {
         'page_title' : 'Home'
    }


    template_name = None;
    if request.user.is_authenticated:
        # Logika Untuk User
        template_name = 'index_user.html'
    else:
        # Logika untuk anonymous user
        template_name = 'index_anonymous.html'

    return render(request, template_name, context)



def LoginView(request):
    context = {
        'page_title' : 'LOGIN'
    }

    user = None

    if request.method == "GET":
        if request.user.is_authenticated:
            # Logika untuk user
            return redirect('index')
        else:
            # Logika untuk anonymous user
            return render(request, 'login.html', context)




    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']


        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
            


@login_required
def LogoutView(request):
    context = {
        'page_title' : 'logout'
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit Query": 
            logout(request)
        return redirect('index')

    return render(request, 'logout.html', context)

















#    username_ucup = 'admin'
#    password_ucup = 'admin123'

#    user = authenticate(request, username=username_ucup, password=password_ucup)
#    print(user)

#    login(request, user)