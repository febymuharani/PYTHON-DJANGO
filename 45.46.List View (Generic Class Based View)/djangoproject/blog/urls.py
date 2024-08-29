from django.urls import path,re_path
from .views import index, ArtikelListView
from django.views.generic import ListView
from .models import Artikel

app_name = 'blog'

urlpatterns = [
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list')
    #path('', ListView.as_view(model=Artikel), name='list')
]