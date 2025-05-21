from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('',include('home.urls')),
    path('', RedirectView.as_view(url ='/home/',permanent=False),name='home'),
    path('admin/', admin.site.urls),
]