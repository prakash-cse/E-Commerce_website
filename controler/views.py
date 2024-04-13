from django.shortcuts import render,redirect
from .form import CreaterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView

def Chome(request):
    return render(request,"admin_panel/home.html")

def Cregister(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created')
            return redirect('Clogin')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('Register')
    else:
        form=CreaterUserForm()
        return render(request,"admin_panel/register.html",{'form':form})

def Clogin(request):

    return render(request, 'admin_panel/login.html')
  