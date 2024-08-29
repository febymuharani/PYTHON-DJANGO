from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import BlogHomeView 

urlpatterns = [
    path('cerpen/', include('cerpen.urls', namespace='cerpen')),
    path('', BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
