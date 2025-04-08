from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('',include('login.urls')),
    path('',include('home.urls')),
    path('', RedirectView.as_view(url ='/login/',permanent=False),name='login'),
    path('admin/', admin.site.urls),
]