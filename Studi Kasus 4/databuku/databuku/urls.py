from django.contrib import admin
from django.urls import path, include
from .views import BlogHomeView, LoginView, Logout


urlpatterns = [
    path('logout/', Logout, name='logout'),
    path('cerpen/', include('cerpen.urls', namespace='cerpen')),
    path('', LoginView, name='login'),
    path('home/', BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
