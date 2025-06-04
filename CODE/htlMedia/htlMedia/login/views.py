from django.shortcuts import render, redirect
from ldap3 import Server, Connection, ALL, SIMPLE
from ldap3.core.exceptions import LDAPException
from .models import User

from django.shortcuts import render 

def login_view(request):
    print("Login view called")
    return render(request, 'login.html')  # <-- das rendert mit RequestContext

def login(request,username,password):
    user = User.objects.filter(username=username).first()
    if user == None:
        user=User.objects.create(username=username,password = password,roles=1)
    
    request.session['user'] = user.pk
    

def authenticate_ldap(request):
    print("Authenticate LDAP called")
    username = request.POST.get('username')
    password = request.POST.get('password')
    LDAP_SERVER = 'ldaps://ldaps.htlwy.at'
    BASE_DN = 'ou=users,dc=schule,dc=local'
 
    user_dn = f'uid={username},{BASE_DN}'
    server = Server(LDAP_SERVER, port=636, use_ssl=True, get_info=ALL)
    print(f"Connecting to LDAP server: {LDAP_SERVER}")
    
    try:
        conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
        print("Authenticated successfully.")
        conn.unbind()
        login(request,username,password)
        return redirect('home')  # Redirect to a success page or home page
    except LDAPException as e:
        print(f"Authentication failed: {e}")
        return redirect('login')  # Redirect to login page with error message
