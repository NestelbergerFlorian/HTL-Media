from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('authenticate_ldap/',views.authenticate_ldap,name='authenticate_ldap'),
]