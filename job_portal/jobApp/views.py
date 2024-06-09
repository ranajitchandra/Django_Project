from django.shortcuts import render, redirect, get_object_or_404
from jobApp.models import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db.models import Q
# Create your views here.

context={
        'acc_succes' : 'Account create successfull',
        'pass_wrong' : 'Password not match',
        'User_login' : 'Login Successfull',
        'save_data' : 'Post Added',
        'update_profile' : 'Update_Profile',
        'pass_update' : 'Password Updated',
    }

def signup(request):
    
    
    
    if request.method=='POST':
        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        display_name=request.POST.get('display_name')
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        user_type=request.POST.get('user_type')
        blood=request.POST.get('blood')
        gender=request.POST.get('gender')
        img=request.FILES.get('img')
        
        
        
        print(display_name,user_name,password,confirm_password,user_type,img,dob,first_name,last_name)
        
        if password==confirm_password:
            user=Custom_User.objects.create_user(
                username=user_name,
                password=confirm_password,
                email=email,
                first_name=first_name,
                last_name=last_name
                )
            user.display_name=display_name
            user.user_type=user_type
            user.dob=dob
            user.blood=blood
            user.gender=gender
            user.image=img
            if user_type == 'recruiter':
                jobrecruiter_profile.objects.create(user = user)
                educationModel.objects.create(user = user)
            else:
                jobseeker_profile.objects.create(user = user)
                educationModel.objects.create(user = user)
            user.save()
            messages.success(request, context['acc_succes'])
            return redirect('signin')
        else:
            messages.warning(request, context['pass_wrong'])
    
    return render(request, 'signup.html')

def signin(request):    
    
    if request.method=='POST':
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user_login=authenticate(username=user_name, password=pass_word)
        
        if user_login:
            login(request, user_login)
            return redirect('dashboard')
        
    return render(request, 'signin.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')


@login_required
def dashboard(request):
    cuser=request.user.username
    print("User name: ",cuser)
    cid=request.user.id
    print("User name: ",cid)
    
    return render(request, 'dashboard.html')


def profile(request):
    data = jobrecruiter_profile.objects.all()
    
    return render(request, 'profile.html', {'data': data})

def add_jobPage(request):

    if request.method=="POST":
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        company_des = request.POST.get('company_des')
        job_des = request.POST.get('job_des')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        salary = request.POST.get('salary')
        date_line = request.POST.get('dob')
        designation = request.POST.get('designation')
        experience = request.POST.get('experience')
        
        createdby = request.user

        save_job = add_job(
            job_title = job_title,
            company_name = company_name,
            company_des = company_des,
            job_des = job_des,
            address = address,
            qualification = qualification,
            salary = salary,
            date_line = date_line,
            designation = designation,
            experience = experience,
            created_by= createdby,
        )
        save_job.save()
        return redirect('view_job')
    return render(request, 'add_job.html')

@login_required
def view_job(request):
    
    get_job = add_job.objects.filter(created_by = request.user)
    
    return render(request, 'view_job.html', {'row' : get_job})



@login_required
def view_job_apply(request):
    
    get_job = add_job.objects.all()
    
    return render(request, 'view_job_apply.html', {'row' : get_job})

@login_required
def seeker_job_apply(request, job_id):
    
    job = get_object_or_404(add_job, id=job_id)
    current_user = request.user
    already_applied = apply_job_model.objects.filter(for_job= job, applicant=current_user).exists()

    if already_applied:
        messages.success(request, "Already Applied")
        return redirect('view_job_apply')
    
    if request.method=="POST":
        skill = request.POST.get('skill')
        qualifications = request.POST.get('qualification')
        profile = request.FILES.get('profile')
        resume = request.FILES.get('resume')
        
        print(skill,qualifications,profile,resume)
        if skill and qualifications and profile and resume:
            app=current_user

            application = apply_job_model(
                skills = skill,
                qualification = qualifications,
                profile_pic = profile,
                resume = resume,
                applicant = app,
                for_job = job,
            )
            application.save()
            return redirect('view_job_apply')
    else:
        context = {
            'jobView' : job
        }
        return render(request, 'seeker_job_apply.html', context)



@login_required
def delete_data(request, job_id):
    get_job = add_job.objects.get(id = job_id)
    get_job.delete()
    return redirect('view_job')



def edit_profile(request):

    return render(request, 'edit_profile.html')

def update_profile(request):
    Current_User=request.user
    if request.method=="POST":
        img=request.FILES.get('img')
        pre_img=request.POST.get('pre_img')
        display_name=request.POST.get('display_name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        skill=request.POST.get('skill')
        work_exp=request.POST.get('work_exp')
        higher_edu=request.POST.get('higher_edu')
        
        company_name=request.POST.get('company_name')
        company_address=request.POST.get('company_address')
        
        
        Password=request.POST.get('Password')
        Confirm_Password=request.POST.get('Confirm_Password')
        
        if Password == Confirm_Password:
            if check_password(Password, Current_User.password):
        
                Current_User.display_name=display_name
                Current_User.dob=dob
                Current_User.gender=gender
                Current_User.blood=blood
                Current_User.save()
                
                if Current_User.user_type == 'jobseeker':
                    my_seeker=Current_User.jobseeker_profile
                    my_seeker.skill=skill
                    my_seeker.work_exp=work_exp
                    my_seeker.highest_edu=higher_edu
                    
                    Current_User.jobseeker_profile.save()
                
                elif Current_User.user_type == 'recruiter':
                    Current_User.jobrecruiter_profile.company_name=company_name
                    Current_User.jobrecruiter_profile.company_address=company_address
                    
                    Current_User.jobrecruiter_profile.save()
                messages.success(request, context['update_profile'])
                return redirect('profile')
        
        
        

def applied_job_by_seeker(request):
    
    applied_obj = apply_job_model.objects.filter(applicant=request.user)
    
    return render(request, 'applied_job_by_seeker.html', {'applied_job':applied_obj})




def posted_job_by_recruiter(request):
    current_user = request.user
    
    post_obj = add_job.objects.filter(created_by=current_user)
    
    return render(request, 'posted_job_by_recruiter.html', {'get_post':post_obj})


def see_applicant(request, myid):
    get_job = get_object_or_404(add_job, id=myid)
    applicant = apply_job_model.objects.filter(for_job=get_job)
    context = {
        'job': get_job,
        'applicant': applicant,
    }
    
    return render(request, 'see_applicant.html', context)

def  reject_application(request, myid):
    applicant = get_object_or_404(apply_job_model, id=myid)
    applicant.status="Rejected"
    applicant.save()
    messages.success(request, "Reject Successfull")
    return redirect('see_applicant', myid=applicant.for_job.id)  

def interviewCall(request, myid):
    interviewdata= get_object_or_404(apply_job_model, id=myid)
    
    interviewdata.status = 'Approved'
    interviewdata.save()
    return redirect('see_applicant', myid=interviewdata.for_job.id)  


def seach_page(request):
    query = request.GET.get('search')
    search = add_job.objects.filter(
        Q(job_title__icontains= query) |
        Q(company_name__icontains= query) |
        Q(company_des__icontains= query) |
        Q(address__icontains= query) |
        Q(salary__icontains= query) |
        Q(created_by__username__icontains= query) 
        )
    context={
        'query' : query,
        'search' : search,
    }

    return render(request, 'seach_page.html', context)


def basic_info(request):

    return render(request, 'basic_info.html')

def education(request):
    
    edu_data=educationModel.objects.filter(user = request.user.id)
    
    return render(request, 'education.html', {'e' : edu_data})


def change_pass(request):
    
    return render(request, 'change_pass.html')

def update_pass(request):
    if request.method=="POST":
        current_pass=request.POST.get('current_pass')
        new_pass=request.POST.get('new_pass')
        conf_pass=request.POST.get('conf_pass')
        
        if check_password(current_pass, request.user.password):
            if new_pass == conf_pass:
                request.user.set_password(new_pass)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, context['pass_update'])
                return redirect('profile')
                
    return render(request, 'change_pass.html')