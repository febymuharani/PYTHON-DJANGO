from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls)
]