from django.shortcuts import render, redirect
from newApp.models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def base(request):
    
    return render(request, 'base.html')

def user_table(request):
    
    user_obj=user_info_model.objects.all()
    
    get_data={
        'user_row' : user_obj
    }
    
    return render(request, 'user_table.html', get_data)

def add_user(request):
    
    if request.method=="POST":
        u_name=request.POST.get('user_name')
        u_email=request.POST.get('email')
        u_password=request.POST.get('password')
        u_img=request.FILES.get('img')
        
        save_user=user_info_model(
            name=u_name,
            email=u_email,
            user_pass=u_password,
            user_img=u_img,
        )
        save_user.save()
        return redirect('user_table')
    
    return render(request, 'add_user.html')
    


def delete_user(request, user_id):
    
    user_obj=user_info_model.objects.get(id=user_id)
    user_obj.delete()
    return redirect('user_table')

def edit_user(request, user_id):
    
    user_obj=user_info_model.objects.filter(id=user_id)
    get_data={
        'user_row' : user_obj
    }
    
    return render(request, 'edit_user.html', get_data)


def index_page(requst):
    
    return render(requst, 'index.html')

def resume_page(request):
    user_obj=user_info_model.objects.all()
    get_data={
        'user_row' : user_obj
    }
    return render(request, 'resume.html', get_data)

def project_page(request):
    
    return render(request, 'projects.html')

def contact_page(request):
    
    return render(request, 'contact.html')


def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        display_name=request.POST.get('display_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        if password==confirm_password:
            save_user=custom_user.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=display_name,
                password=confirm_password,
            )
            save_user.user_type=user_type
            save_user.save()
            return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):
    if request.method=="POST":
        user_name=request.POST.get('display_name')
        pass_word=request.POST.get('password')
        login_user=authenticate(
            username=user_name,
            password=pass_word
        )
        if login_user:
            login(request, login_user)
            return redirect('index_page')
    return render(request, 'signin.html')

def logout_Page(request):
    logout(request)
    return redirect('signin')


