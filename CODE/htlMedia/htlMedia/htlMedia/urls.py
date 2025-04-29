from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',include('login.urls')),
    path('',include('home.urls')),
    path('', views.CheckLogin,name='checkIn'),
    path('admin/', admin.site.urls),
]