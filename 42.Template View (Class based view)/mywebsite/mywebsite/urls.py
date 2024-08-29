"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from .views import IndexView, ContextView, ParameterView

urlpatterns = [
    re_path(r'^parameter/(?P<parameter1>[0-9]+)/(?P<parameter2>[0-9]+)$', ParameterView.as_view()),
    path('context/', ContextView.as_view()),
    path('default/', TemplateView.as_view(template_name='default.html')), # 2
    path('', IndexView.as_view(template_name='index.html')), # 1
    path('admin/', admin.site.urls), 
]


# 1.Membuat class view di views.py, tapi menggunakan templatenya di url/
# isi dari class kosong kita memasukkan template html nya lansung di urls.py 
# dengan template_name

# 2.Jika halaman itu statis, tidak ada perubahan apapun,maka dilakukan langsung TemplateView pada urls.py
# kita tidak membuat class pada views.py tapi bisa membuat nya langsung dengan memasukkan TemplateView dan html pada template_name nya

# 3.Membuat views dengan context saja, kita menggunakan TemplateView di Views.py 
# kita membuat class views berisi context dan mengimport nama class pada import .views dan menggunakan
# TemplateView d dalam (class)

# 4.Kita memasukan parameter kedalam template, dengan menggunakan regex
