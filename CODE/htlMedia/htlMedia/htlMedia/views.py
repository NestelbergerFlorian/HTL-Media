from django.shortcuts import render, redirect

def CheckLogin(request):
    print(request.user)
    if request.user.is_authenticated: return redirect('home')
    else: return redirect('login_test')