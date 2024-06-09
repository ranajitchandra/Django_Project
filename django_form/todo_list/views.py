from django.shortcuts import render, redirect
from todo_list.models import *
from django_form.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.



def signupPage(request):
    
    if request.method == "POST":
        
        form = myUserCreationForm(request.POST,request.FILES)
        
        print(form.is_valid())
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Sign up Successfull")
            
            return redirect('signinPage')
    else:
        form = myUserCreationForm(request.POST,request.FILES)
        
    context = {
        
        'form':form
    }
    return render(request, 'signup.html', context)


def signinPage(request):
    
    if request.method=="POST":
        signinForm = myAuthenticationForm(request, data=request.POST)
        if signinForm.is_valid():
            i = signinForm.get_user()
            login(request,i)
            messages.success(request, "Sign up Successfull")
            return redirect('dashboard')
    else:
        signinForm = myAuthenticationForm()
        
    context = {
        'form' : signinForm
    }
    return render(request, 'signin.html', context)


def dashboard(request):
    
    return render(request, 'dashboard.html')