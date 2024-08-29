from django.urls import path,re_path

from .views import CerpenListView, CerpenDetailView, CerpenKategoriView, CerpenCreateView, CerpenManageView, CerpenDeleteView, CerpenUpdateView

app_name = 'cerpen'

urlpatterns = [
    re_path(r'^manage/update/(?P<pk>\d+)$', CerpenUpdateView.as_view(), name='update'),
    re_path(r'^manage/delete/(?P<pk>\d+)$', CerpenDeleteView.as_view(), name='delete'),
    path('manage/', CerpenManageView.as_view(), name='manage'),
    path('tambah/', CerpenCreateView.as_view(), name='create'),
    re_path(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$', CerpenKategoriView.as_view(), name='category'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', CerpenDetailView.as_view(), name='detail'),
    re_path(r'^(?P<page>\d+)$', CerpenListView.as_view(), name='list'),
]