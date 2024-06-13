from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.http import HttpResponse
from myApp.models import *
from myProject.forms import *

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import date



def signupPage(request):

    if request.method =='POST':

        form=myUserCreationForm(request.POST,request.FILES)

        print(form.is_valid())

        if form.is_valid():

            form.save()

            messages.success(request,"Signup Successfully")

            return redirect("signinPage")
    else:
        
        form=myUserCreationForm(request.POST)
   
    context={
        'form':form
    }

    return render(request,"signupPage.html",context)


def signinPage(request):

    if request.method=="POST":

        signinForm=myAuthenticationForm(request,data=request.POST)

        if signinForm.is_valid():

            i=signinForm.get_user()

            login(request,i)

            return redirect("dashboardPage")
    else:
        signinForm=myAuthenticationForm()
    
    context={
        "signinForm":signinForm
    }

    return render(request,"signinPage.html",context)


@login_required
def logoutPage(request):

    logout(request)
    return redirect("signinPage")

@login_required
def categoryPage(request):

    if request.method=="POST":

        current_user=request.user

        form=CategoryForm(request.POST)

        if form.is_valid():

            category=form.save(commit=False)

            category.user=current_user

            category.save()

            return redirect("categorylist")
    else:
        form=CategoryForm()
    
    context={
        'form':form
    }

    return render(request,"categoryPage.html",context)



def createTaskPage(request):

    if request.method=="POST":

        form=CreateTaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("taskList")
    else:
        form=CreateTaskForm()
    
    context={
        'form':form
    }


    return render(request,"createTaskPage.html",context)

@login_required
def categorylist(request):
    cat=CategoryModel.objects.all()

    return render(request,"categorylist.html", {'cat':cat})


@login_required

def taskList(request):

    task=TaskModel.objects.all()


    return render(request,"taskList.html",{"task":task})


def DeleteTaskPage(request,myid):

    task=get_object_or_404(TaskModel,id=myid)
    task.delete()

    return redirect("taskList")


def editTaskPage(request,myid):
    task=get_object_or_404(TaskModel,id=myid)
    
    if request.method=="POST":

        form=CreateTaskForm(request.POST,instance=task)

        if form.is_valid():

            form.save()

            return redirect("taskList")
    else:
        form=CreateTaskForm(instance=task)
    
    context={
        'form':form
    }
    
    return render(request,"editTaskPage.html",context)


def  finishTaskPage(request, myid):
    task = get_object_or_404(TaskModel, id=myid)
    task.status="Done"
    task.save()
    return redirect('taskList')  
def  dash_finishTaskPage(request, myid):
    task = get_object_or_404(TaskModel, id=myid)
    task.status="Done"
    task.save()
    return redirect('dashboardPage')  

@login_required
def dashboardPage(request):
    task_upcoming = TaskModel.objects.filter(due_date__gt=date.today())
    done = TaskModel.objects.filter(status='Done')
    upcoming_count = TaskModel.objects.filter(status='On_Going').count()
    done_count = TaskModel.objects.filter(status='Done').count()
    context = {
        'task_upcoming': task_upcoming,
        'upcoming_count': upcoming_count,
        'done_count': done_count,
        'done': done
    }

    return render(request,"dashboardpage.html", context)
