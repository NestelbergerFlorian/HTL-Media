from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .froms import PostForm,FilterForm
from .models import Post


def home(request):
 if request.method == 'POST':
  form = PostForm(request.POST, request.FILES)
  if form.is_valid():
   return uploadPicture(request,form)
  form = FilterForm(request.POST, request.FILES)
  if form.is_valid():
   return filteredView(request,form)
 else:
   form = PostForm()
   filterForm = FilterForm()
   data = Post.objects.all()
   return render(request, 'home.html', {'form': form,'filterForm':filterForm,'data':data})
 
def success(request):
 return HttpResponse('successfully uploaded')

def uploadPicture(request, form):
  post = form.save(commit=False)
  post.uploaded_by = request.session.get('user',None)
  post.uploaded_at = timezone.now()
  form.save()
  form = PostForm()
  filterForm = FilterForm()
  data = Post.objects.all()
  return render(request, 'home.html', {'form': form,'filterForm':filterForm,'data':data})

def filteredView(request,form):
  post = form.save(commit=False)
  form = PostForm()
  filterForm = FilterForm()
  data = Post.objects.filter(titel__icontains=post.titel)
  return render(request, 'home.html', {'form': form,'filterForm':filterForm,'data':data})
