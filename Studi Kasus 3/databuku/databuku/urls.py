from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import LoginView, Logout
from .views import BlogHomeView 

urlpatterns = [
    path('logout/', Logout, name='logout'),
    path('', LoginView, name='login'),
    path('cerpen/', include('cerpen.urls', namespace='cerpen')),
    path('login/home', BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
