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

def filteredView(request):
  form = FilterForm(request.POST, request.FILES)
  user  = User.objects.get(pk=request.session.get('user',None))
  
  print(form.data.get("order_by"))
  if form.data.get("order_by") == '1':
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('uploaded_at')
  elif form.data.get("order_by") == '2':
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('-uploaded_at')
  elif form.data.get("order_by") == '3':
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('views')
  elif form.data.get("order_by") == '4':
    data = Post.objects.filter(titel__icontains=form.data.get("titel")).order_by('likes')
  elif form.data.get("order_by") == '5':
    data = Post.objects.filter(titel__icontains=form.data.get("titel"),uploaded_by=user).order_by('uploaded_at')
  else:
    data  = Post.objects.all().order_by('uploaded_at')

  form = PostForm()
  filterForm = FilterForm()
  users = User.objects.all()
  return render(request, 'home.html', {'form': form,'filterForm':filterForm,'data':data,'user':user,'users':users})

def uploadPost(request):
  form = PostForm(request.POST,request.FILES)
  if form.is_valid():
    post = form.save(commit=False)
    user = User.objects.get(pk=request.session.get('user',None))
    post.likes = 0
    post.views = 0
    post.uploaded_by = user
    post.uploaded_at = timezone.now()
    form.save()
  return redirect('/home')

def deletePost(request,pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return redirect('/home')

def likePost(request,pk):
    post = get_object_or_404(Post, pk=pk)
    user = User.objects.get(pk=request.session.get('user',None))
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    post.save()
    return redirect("/home/view/"+str(pk))

def viewPost(request,pk):
  post = get_object_or_404(Post, pk=pk)
  post.views = post.views+1
  post.save()
  return redirect("/home/view/"+str(pk))

def postView(request,pk):
  post = get_object_or_404(Post, pk=pk)
  user = User.objects.get(pk=request.session.get('user',None))
  form = PostForm()
  filterForm = FilterForm()
  data = Post.objects.all().order_by('-uploaded_at')
  users = User.objects.all()
  return render(request, 'home.html', {'user':user,'form': form,'filterForm':filterForm,'data':data,'users':users,'post':post})
