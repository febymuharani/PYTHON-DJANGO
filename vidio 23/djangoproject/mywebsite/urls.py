from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<int:input>/', views.angka, name='angka'),
    path('<int:tahun>/<int:bulan>/<int:hari>/', views.tanggal, name='tanggal'),
    path('<str:page>/', views.link, name='link'),
]
