from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/delete/<int:pk>',views.deletePost,name='delete'),
    path('home/upload',views.uploadPost,name='upload'),
    path('home/filtername',views.filteredView,name='filter')
]