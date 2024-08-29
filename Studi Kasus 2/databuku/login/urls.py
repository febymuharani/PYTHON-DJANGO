from django.urls import path
from .views import LoginView, LogoutView

app_name = 'login'

urlpatterns = [
    path('logout/', LogoutView, name='logout'),
    path('', LoginView, name='login'),
]