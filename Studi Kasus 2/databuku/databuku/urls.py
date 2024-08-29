from django.contrib import admin
from django.urls import path, include
from .views import BlogHomeView 

urlpatterns = [
    path('login/', include('login.urls', namespace='login')),
    path('cerpen/', include('cerpen.urls', namespace='cerpen')),
    path('', BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
