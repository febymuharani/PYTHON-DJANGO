from django.contrib import admin
from django.urls import path

from .views import index, IndexView, LoginView, LogoutView

urlpatterns = [
    path('logout/', LogoutView, name='logout'),
    path('login/', LoginView, name="login"),
 #   path('', IndexView.as_view(), name="index"),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
]
