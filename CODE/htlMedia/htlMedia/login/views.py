from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login(request):
 template = loader.get_template('login.html')
 return HttpResponse(template.render())

def login_test_view(request):
    form = AuthenticationForm()
    return render(request, 'login_test.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ersetzen Sie 'home' durch Ihre gewünschte Ziel-URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
