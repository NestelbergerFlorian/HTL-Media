from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/delete/<int:pk>',views.deletePost,name='delete'),
    path('home/like/<int:pk>',views.likePost,name='like'),
    path('home/firstview/<int:pk>',views.viewPost,name='like'),
    path('home/view/<int:pk>',views.postView,name='like'),
    path('home/form',views.form,name='form'),
    path('home/upload',views.uploadPost,name='upload'),
    path('home/logout',views.logout,name='logout'),
    path('home/filter',views.filteredView,name='filter')
]