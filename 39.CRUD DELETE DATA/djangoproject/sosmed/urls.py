from django.urls import path, re_path
from . import views

app_name = 'sosmed'

urlpatterns = [
    re_path('delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path('update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('',  views.list,name='list'),
]