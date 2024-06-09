from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from jobPortalApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

def signUpPage(request):

    context={
        'Acc_Success_Message':'Account Create Successfully',
        'Password_not_match':'Password and Confirmed Password Does not Mathced',
    }

    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        profile_picture=request.FILES.get('profile_picture')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        usertype=request.POST.get('usertype')


        if password==confirm_password:
            myUser=customUserModel.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password,
                profile_picture=profile_picture,
                gender=gender,
                address=address,
                date_of_birth=dob,
                user_type=usertype,
            )
            if usertype == 'recruiter':

                JobRecruiterProfile.objects.create(user= myUser)

            elif usertype == 'seeker':

                data=JobSeekerProfile(
                    user=myUser,
                )
                data.save()

            myUser.save()
            messages.success(request,context['Acc_Success_Message'])
            return redirect('signInPage')
        
        else:
            messages.warning(request,'Password_not_match')

        
    return render(request, 'signUp.html')

def signInPage(request):

    if request.method=='POST':

        UserName=request.POST.get('username')
        PassWord=request.POST.get('password')

        print(UserName,PassWord)

        user=authenticate(username=UserName,password=PassWord)

        print(user)

        if user:
            login(request,user)
            return redirect('dashboard')
        
        else:
            return redirect('signInPage')
        
    return render(request, 'signIn.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logoutfn(request):
    logout(request)
    return redirect('signInPage')

@login_required
def profile(request):
    
    return render(request, 'profile.html')


@login_required
def addjobform(request):
    if request.method=='POST':
        job_titel=request.POST.get('job_titel')
        company_name=request.POST.get('company_name')
        address=request.POST.get('address')
        job_desciption=request.POST.get('job_desciption')
        company_desciption=request.POST.get('company_desciption')
        qualification=request.POST.get('qualification')
        salary=request.POST.get('salary')

        current_user = request.user

        user=job_model(
            job_titel=job_titel,
            company_name=company_name,
            address=address,
            job_desciption=job_desciption,
            company_desciption=company_desciption,
            qualification=qualification,
            salary=salary,
            created_by=current_user
        )
        user.save()
        return redirect('viewslist')

    return render(request, 'addjobform.html')

@login_required
def editProfilePage(request):

    Current_User=request.user

    if request.method=='POST':

        image=request.FILES.get("profile_picture")
        gender=request.POST.get("gender")
        address=request.POST.get("address")
        date_of_birth=request.POST.get("date_of_birth")


        password=request.POST.get("password")
        Confirm_Password=request.POST.get("Confirm_Password")

        skills=request.POST.get("skills")
        work_experience=request.POST.get("work_experience")

        company_name=request.POST.get("company_name")
        company_address=request.POST.get("company_address")
        

        if password==Confirm_Password:

            if check_password(password, Current_User.password):

                Current_User.gender=gender
                Current_User.address=address
                Current_User.date_of_birth=date_of_birth

                if Current_User.user_type == 'seeker':

                    Current_User.jobseekerprofile.skils=skills
                    Current_User.jobseekerprofile.work_experience=work_experience
                    Current_User.jobseekerprofile.save()

                elif Current_User.user_type == 'recruiter':

                    myRecruiter=Current_User.jobrecruiterprofile
                    myRecruiter.company_name=company_name
                    myRecruiter.company_address=company_address
                    myRecruiter.save()
                
                Current_User.save()


                return redirect("BasicInformation")


    return render(request,'editProfile.html')

def BasicInformation(request):


    return render(request,'BasicInformation.html')

def EducationQualification(request):


    return render(request,'EducationQualification.html')


def changePasswordPage(request):

    if request.method=='POST':

        Current_Password=request.POST.get("Current_Password")
        New_password=request.POST.get("New_password")
        Confirm_New_Password=request.POST.get("Confirm_New_Password")

        if check_password(Current_Password,request.user.password):

            if New_password==Confirm_New_Password:

                request.user.set_password(New_password)

                request.user.save()

                update_session_auth_hash(request,request.user)

                return redirect("profile")

    return render(request,'changePasswordPage.html')


@login_required
def jobPosterbyRecruiter(request):

    current_user=request.user

    postjob=job_model.objects.filter(created_by=current_user)

    context={
        'postjob':postjob
    }

    return render(request,"jobPosterbyRecruiter.html",context)


@login_required
def appliedjobbySeeker(request):

    current_user=request.user

    applyjob=jobApplyModel.objects.filter(applicant=current_user)

    context={
        "applyjob":applyjob,
    }


    return render(request,"appliedjobbySeeker.html",context)


@login_required
def viewslist(request):

    current_user=request.user
    
    obj= job_model.objects.all()
    
    myJob=[]

    for job in obj:

        already_applied=jobApplyModel.objects.filter(job=job,applicant=current_user).exists()

        myJob.append((job,already_applied))


    mydict={
        'myJob':myJob
    }
    return render(request,"viewslist.html", mydict)

def seekerApplyPage(request,myid):
    user=request.user
    job=get_object_or_404(job_model,id=myid)

    already_applied=jobApplyModel.objects.filter(job=job,applicant=user).exists()

    # if already_applied:

    #     messages.warning(request,"Already Applied")

    #     return redirect("viewslist")


    if request.method=="POST":

        skills=request.POST.get("skills")
        resume=request.FILES.get("resume")
        picture=request.FILES.get("picture")
        qualifications=request.POST.get("qualifications")


        if skills and resume and picture and qualifications:

            applicant=user

            application=jobApplyModel(
                skills=skills,
                resume=resume,
                profile_picture=picture,
                qualification=qualifications,
                job=job,
                applicant=applicant
            )
            application.save()

            messages.success(request,"Application Submit Successfully")

            return redirect("appliedjobbySeeker")
    else:
        context={
        'job':job,
        "already_applied":already_applied
        }
        return render(request,"seekerApplyPage.html",context)
    

def totalApplicants(request,myid):

    job=get_object_or_404(job_model,id=myid)

    applicants=jobApplyModel.objects.filter(job=job)

    context={
        "job":job,
        "applicant":applicants
    }


    return render(request,"totalApplicants.html",context)

def callforInterview(request,myid):
    
    applicant=get_object_or_404(jobApplyModel,id=myid)

    applicant.status="Approved"

    applicant.save()

    messages.success(request,"Application Approved Successfully")

    return redirect("totalApplicants", myid=applicant.job.id)


def applicationReject(request,myid):

    i=get_object_or_404(jobApplyModel,id=myid)

    i.status="Rejected"

    i.save()

    messages.success(request,"Application Reject Successfully")

    return redirect("totalApplicants", myid=i.job.id)




