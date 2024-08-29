from django.urls import path, re_path
from .views import (
    SosmedListView,
    SosmedDeleteView,
    SosmedFormView,
)

app_name = 'sosmed'

urlpatterns = [
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', SosmedDeleteView.as_view(), name='delete'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', SosmedFormView.as_view(mode='update'), name='update'),
    path('create/', SosmedFormView.as_view(), name='create'),
    path('', SosmedListView.as_view(), name='list'),
]