from django.http import HttpResponse
from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .froms import PostForm

def home(request):
  print("Hallo World")	
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.uploaded_by = request.user
      post.uploaded_at = timezone.now()
      form.save()
      return redirect('success')
  else:
    form = PostForm()
    return render(request, 'home.html', {'form': form})
 
def success(request):
 return HttpResponse('successfully uploaded')