from django.urls import path, re_path


from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name = 'index')
]