from django.urls import path,re_path
from .views import ArtikelListView, ArtikelDetailView, ArtikelFormView, ArtikelCreateView1, ArtikelCreateView2
from django.views.generic import ListView, DetailView, FormView
from .models import Artikel
from .forms import ArtikelForm



app_name = 'blog'

urlpatterns = [
    path('create/', ArtikelCreateView2.as_view(), name='create'),
    #path('create/', ArtikelCreateView1.as_view(), name='create'),
    #path('create/', ArtikelFormView.as_view(), name='create'),
    #path('create/', FormView.as_view(form_class=ArtikelForm, template_name='blog/create.html'), name='create'),
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    re_path(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
    #re_path(r'^detail/(?P<slug>[\w-]+)$', DetailView.as_view(model=Artikel), name='detail'),
    #path('', ListView.as_view(model=Artikel), name='list')
]