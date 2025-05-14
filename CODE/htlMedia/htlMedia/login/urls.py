from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.login_view, name='login_test'),
    #path('login/',views.login,name='login'),
]