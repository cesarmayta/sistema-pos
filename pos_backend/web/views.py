from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_usuario(request):
    context = {
                'msg_error':'nn'
            }
    if request.method == 'POST':
        usuario = request.POST['username']
        password = request.POST['password']
        
        usuario = authenticate(request,username=usuario,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            context = {
                'msg_error':'datos incorrectos'
            }
    return render(request,'login.html',context)

@login_required(login_url='/login')
def index(request):
    return render(request,'index.html')

def logout_usuario(request):
    logout(request)
    return redirect('/')