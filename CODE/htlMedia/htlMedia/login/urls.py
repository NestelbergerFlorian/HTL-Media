from django.urls import path
from . import views
from home import views as home_views

urlpatterns = [
    path('home/', home_views.home, name='home'),
    path('login/',views.login_view,name='login'),
    path('authenticate_ldap/',views.authenticate_ldap,name='authenticate_ldap'),
]