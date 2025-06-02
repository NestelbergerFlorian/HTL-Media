from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import logout
from .froms import PostForm,FilterForm
from .models import Post
from login.models import User


def home(request):
  user = User.objects.get(pk=request.session.get('user',None))
  form = PostForm()
  filterForm = FilterForm()
  data = Post.objects.all().order_by('-uploaded_at')
  users = User.objects.all()
  return render(request, 'home.html', {'user':user,'form': form,'filterForm':filterForm,'data':data,'users':users})

def uploadPost(request):
  form = PostForm(request.POST,request.FILES)
  if form.is_valid():
    post = form.save(commit=False)
    user = User.objects.get(pk=request.session.get('user',None))
    post.uploaded_by = user
    post.uploaded_at = timezone.now()
    form.save()
  return redirect('/home')

def deletePost(request,pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return redirect('/home')

def filteredView(request):
  form = FilterForm(request.POST, request.FILES)
  print(form.data.get("order_by"))
  if(form.data.get("order_by") == '2'):
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('-uploaded_at')
  else:
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('uploaded_at')
  form = PostForm()
  filterForm = FilterForm()
  data  = Post.objects.all()
  users = User.objects.all()
  user  = User.objects.get(pk=request.session.get('user',None))
  return render(request, 'home.html', {'form': form,'filterForm':filterForm,'data':data,'user':user,'users':users})
