from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('login-test/', login_test_view, name='login_test'),
    path('login/',views.login,name='login'),
]