from django.shortcuts import render
from django.contrib.auth import authenticate , login, logout
from .forms import FormLogin
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def Home(request):
    return render(request, 'login/home')

def LoginView(request):
    form = FormLogin
    if request.method == "POST":
        username_user = request.POST['username']
        password_user = request.POST['password']

        user = authenticate(request, username=username_user, password=password_user)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login/login.html', {'form':form})


def LogoutView(request):
    logout(request)
    request.session.flush
    return redirect('/login/')