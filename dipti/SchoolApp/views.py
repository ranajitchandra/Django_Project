from django.shortcuts import render, redirect
from SchoolApp.models import *
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

# Create your views here.



def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')



def admin_dashboard(request):
    return render(request, 'admin_Page/admin-dashboard.html')

def teacher_dashboard(request):
    return render(request, 'admin_Page/teacher-dashboard.html')

def student_dashboard(request):
    return render(request, 'admin_Page/student-dashboard.html')



# student
def students(request):
    return render(request, 'student/students.html')

def student_view(request):
    return render(request, 'student/student-details.html')

def add_student_page(request):
    dep = department.objects.all()
    
    if request.method=="POST":
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        std_id=request.POST.get('std_id')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        religion=request.POST.get('religion')
        Joining_date=request.POST.get('Joining_date')
        phone=request.POST.get('phone')
        section=request.POST.get('section')
        img=request.FILES.get('img')
        father_name=request.POST.get('father_name')
        father_occu=request.POST.get('father_occu')
        father_phone=request.POST.get('father_phone')
        father_email=request.POST.get('father_email')
        mother_name=request.POST.get('mother_name')
        mother_occu=request.POST.get('mother_occu')
        mother_phone=request.POST.get('mother_phone')
        mother_email=request.POST.get('mother_email')
        present_address=request.POST.get('present_address')
        permanent_address=request.POST.get('permanent_address')
        dep_id=request.POST.get('dep')
        
        save_std = add_student(
            f_name=f_name,
            l_name=l_name,
            std_id=std_id,
            gender=gender,
            dob=dob,
            religion=religion,
            Joining_date=Joining_date,
            phone=phone,
            section=section,
            img=img,
            father_name=father_name,
            father_occu=father_occu,
            father_phone=father_phone,
            father_email=father_email,
            mother_name=mother_name,
            mother_occu=mother_occu,
            mother_phone=mother_phone,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address,
            department_add=dep_id,
        )
        save_std.save()
        return redirect('students')
    
    return render(request, 'student/add-student.html',{'departments' : dep})

def edit_student(request):
    return render(request, 'student/edit-student.html')



def teachers(request):
    return render(request, 'teacher/teachers.html')

def teacher_view(request):
    return render(request, 'teacher/teacher-details.html')

def add_teacher(request):
    return render(request, 'teacher/add-teacher.html')

def edit_teacher(request):
    return render(request, 'teacher/edit-teacher.html')



def departments(request):
    dep_list=department.objects.all()
    dep_data=[]
    for department in dep_list:
        print(add_student.objects.filter(department_add=department).count())
        std_count=add_student.objects.filter(department_add=department).count()
        dep_data.append(
            {
                "Total_student" : std_count,
                "Department_name" : department.department_name,
                "HOD" : department.department_head_name,
                "ID" : department.id,
            }
        )
        context={
            'department_list': dep_data
        }
    return render(request, 'department/departments.html', context)

def add_department(request):
    
    if request.method=="POST":
        dep_name =request.POST.get('dep_name')
        dep_head =request.POST.get('dep_head')
        if department.objects.filter(department_name=dep_name).exists():
            
            return redirect('add_department')
        else:
            save_dep = department(
                department_name=dep_name,
                department_head_name=dep_head,
            )
            save_dep.save()
            messages.warning('Department Add Successfull')
            return redirect('departments')
    return render(request, 'department/add-department.html')

def edit_department(request):
    return render(request, 'department/edit-department.html')



# Subject

def subjects(request):
    return render(request, 'subject/subjects.html')

def add_subject(request):
    dep = department.objects.all()
    
    return render(request, 'subject/add-subject.html',{'departments' : dep})
    
def edit_subject(request):
    return render(request, 'subject/edit-subject.html')




#department

def fees_collections(request):
    return render(request, 'accounts/fees-collections.html')

def expenses(request):
    return render(request, 'accounts/expenses.html')

def salary(request):
    return render(request, 'accounts/salary.html')

def add_fees_collection(request):
    return render(request, 'accounts/add-fees-collection.html')

def add_expenses(request):
    return render(request, 'accounts/add-expenses.html')

def add_salary(request):
    return render(request, 'accounts/add-salary.html')

def holiday(request):
    return render(request, 'management/holiday.html')

def fees(request):
    return render(request, 'management/fees.html')

def exam(request):
    return render(request, 'management/exam.html')

def event(request):
    return render(request, 'management/event.html')

def time_table(request):
    return render(request, 'management/time-table.html')

def library(request):
    return render(request, 'management/library.html')



def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_login= authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            if request.user.user_type=='1':
                return redirect('admin_dashboard')
            elif request.user.user_type=='2':
                return redirect('teacher_dashboard')
            elif request.user.user_type=='3':
                return redirect('student_dashboard')
            else:
                return redirect('loginPage')
            
    return render(request, 'login.html')


def signupPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        print(username)
        if password == password2:
            user = custom_user.objects.create_user(username=username, password=password)
            user.email=email
            user.user_type="1"
            user.save()
            return redirect("index")
        else:
            return redirect("signupPage")
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect("loginPage")
