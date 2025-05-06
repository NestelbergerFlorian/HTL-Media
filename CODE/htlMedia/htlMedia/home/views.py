from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .froms import PostForm
from .models import Post


def home(request):
 if request.method == 'POST':
  form = PostForm(request.POST, request.FILES)
  if form.is_valid():
   post = form.save(commit=False)
   post.uploaded_by = request.user
   post.uploaded_at = datetime.now()
   form.save()
   return redirect('success')
 else:
   form = PostForm()
   data = Post.objects.all()
   print(data)
   return render(request, 'home.html', {'form': form,'data':data})
 
def success(request):
 return HttpResponse('successfully uploaded')