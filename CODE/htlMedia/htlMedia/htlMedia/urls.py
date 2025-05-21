from django.contrib import admin
from django.urls import include, path

from . import views

from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',include('login.urls')),
    path('',include('home.urls')),
    path('', views.CheckLogin,name='checkIn'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login_test'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]