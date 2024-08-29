from django.urls import path
from .views import ArtikelIndexViews, ArtikelAddView, ArtikelAddView2, OtongView

app_name = 'artikel'

urlpatterns = [
    path('otong/', OtongView, name='otong'),
    path('add2/', ArtikelAddView2, name='add2'),
    path('add/', ArtikelAddView, name='add'),
    path('', ArtikelIndexViews, name='index')
]