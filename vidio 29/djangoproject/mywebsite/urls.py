from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', include('contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),
]
