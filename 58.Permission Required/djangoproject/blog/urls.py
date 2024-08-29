from django.urls import path

from .views import AddView, IndexViews, UpdateView

app_name = 'blog'

urlpatterns = [
    path('update/', UpdateView, name='update'),
    path('add/', AddView, name='add'),
    path('', IndexViews, name='index')
]