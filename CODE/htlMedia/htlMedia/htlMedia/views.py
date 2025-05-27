from django.shortcuts import render, redirect

def CheckLogin(request):
    print(request.user)
    if request.session.get('user',None): return redirect('home')
    else: return redirect('login')