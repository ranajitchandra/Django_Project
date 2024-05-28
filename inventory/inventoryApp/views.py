from django.shortcuts import render, redirect
from inventoryApp.models import custom_user, add_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin_Page(request):
    if request.method=="POST":
        user_name=request.POST.get('user_name')
        Password=request.POST.get('password')
        user_login=authenticate(username=user_name,password=Password)
        if user_login:
            login(request, user_login)
            return redirect('view_data_page')
    return render(request, 'signin.html')

def logout_page(request):
    logout(request)
    return redirect('signin_Page')

def signup_Page(request):
    if request.method=="POST":
        display_name=request.POST.get('display_name')
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_email=request.POST.get('user_email')
        user_type=request.POST.get('user_type')
        img=request.FILES.get('img')
        if password==confirm_password:
            save_data=custom_user.objects.create_user(
                username=user_name,
                password=confirm_password,
                email=user_email
            )
            save_data.display_name=display_name
            save_data.user_type=user_type
            save_data.image=img
            save_data.save()
            return redirect('signin_Page')
    
    return render(request, 'signup.html')
@login_required
def view_data_page(request):
    get_data=add_data.objects.filter(which_user = request.user)
    return render(request, 'view_data.html', {'data' : get_data})
    
def homepage(request):
    return render(request, 'home.html')

def add_data_page(request):
    if request.method=="POST":
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        company_des=request.POST.get('company_des')
        get_user=request.user
        save_data=add_data(
            title=job_title,
            c_name=company_name,
            c_des=company_des,
            which_user=get_user,
        )
        save_data.save()
        return redirect('view_data_page')
    return render(request, 'add_data.html')
    
def delete_data(request, delid):
    delete_data=add_data.objects.get(id=delid)
    delete_data.delete()
    return redirect('view_data_page')

def edit_data_page(request, editid):
    get_data=add_data.objects.get(id=editid)
    return render(request, 'edit_data.html', {'data' : get_data})

def update_data(request):
    if request.method=="POST":
        data_id=request.POST.get('data_id')
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        company_des=request.POST.get('company_des')
        save_data=add_data(
            id=data_id,
            title=job_title,
            c_name=company_name,
            c_des=company_des,
            which_user= request.user
        )
        save_data.save()
        return redirect('view_data_page')