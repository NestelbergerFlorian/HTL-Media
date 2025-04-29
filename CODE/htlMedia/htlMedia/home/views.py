from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

def home(request):
 template = loader.get_template('home.html')
 return HttpResponse(template.render())