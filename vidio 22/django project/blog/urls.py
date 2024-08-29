from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('jurnal/', views.jurnal),
    path('cerpen/', views.cerpen),
    path('berita/', views.berita),
]