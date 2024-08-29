from django.urls import path, re_path


from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^khusus/(?P<input>[\w-]+)$', views.khusus, name="khusus"),
    re_path(r'^category/$', views.categoryPost, name="category"),
    re_path(r'^single/$', views.singlePost, name="single"),
    path('', views.index, name="index")
]