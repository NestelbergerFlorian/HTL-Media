from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .froms import PostForm,FilterForm
from .models import Post


def home(request):
  print("Hallo World")	
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      print(request.session.get('user',None))
      post.uploaded_by = request.session.get('user',None)
      post.uploaded_at = timezone.now()
      form.save()
  form = PostForm()
  return render(request, 'home.html', {'form': form})