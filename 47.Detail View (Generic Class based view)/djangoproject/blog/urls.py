from django.urls import path,re_path
from .views import ArtikelListView, ArtikelDetailView
from django.views.generic import ListView, DetailView
from .models import Artikel

app_name = 'blog'

urlpatterns = [
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    re_path(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
    #re_path(r'^detail/(?P<slug>[\w-]+)$', DetailView.as_view(model=Artikel), name='detail'),
    #path('', ListView.as_view(model=Artikel), name='list')
]