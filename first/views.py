from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Ntodo
from .forms import Ntodoform
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'tempfirst/home.html')

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                u=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                u.save()
                return redirect('ulogin')
            except IntegrityError:
                return render(request,'tempfirst/signup.html')
            
    return render(request,'tempfirst/signup.html')

def ulogin(request):
    if request.method=='POST':
        a=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if a is not None:
            login(request,a)
            return redirect('start')
        else:
            return render(request,'tempfirst/ulogin.html')

    return render(request,'tempfirst/ulogin.html')

def start(request):

    return render(request,'tempfirst/start.html')

def createtodo(request):
    if request.method=='POST':
        a=Ntodoform(request.POST)
        b=a.save(commit=False)
        b.user=request.user
        b.save()
        return redirect('start')
    else:
        return render(request,'tempfirst/createtodo.html',{'form':Ntodoform()})


def currenttodo(request):
    todos=Ntodo.objects.filter(user=request.user,datecompleted__isnull=True)
    
    return render(request,'tempfirst/currenttodo.html',{'todos':todos})

def viewtodo(request,id):
    a=get_object_or_404(Ntodo,pk=id,user=request.user)
    if request.method=='POST':
        pass
    else:
        return render(request,'tempfirst/viewtodo.html',{'todo':a})

def complete(request,id):
    if request.method=='POST':
        pass
    else:
        a=get_object_or_404(Ntodo,pk=id,user=request.user)
        a.datecompleted=timezone.now()
        a.save()
        return redirect('currenttodo')

def delete(request,id):
    d=get_object_or_404(Ntodo,pk=id,user=request.user)
    if request.method=='POST':
        pass
    else:
        d.delete()
        return redirect('currenttodo')

def completedtodo(request):
    c=Ntodo.objects.filter(user=request.user,datecompleted__isnull=False)
    return render(request,'tempfirst/completedtodo.html',{'todos':c})



def ulogout(request):
    if request.method=='GET':
        logout(request)
        return redirect('home')