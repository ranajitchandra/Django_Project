from django.shortcuts import render, redirect
from SchoolApp.models import *
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

# Create your views here.

context={
        'acc_succes' : 'Admin Account Create Successfull',
        'pass_wrong' : 'Password not match',
        'User_login' : 'Login Successfull',
        'save_data' : 'Data Added',
        'update' : 'Updated',
        'pass_update' : 'Password Updated',
        'logout_message' : 'Logout Successfull',
        'delete_message' : 'Delete Successfull',
        'date_exists' : 'Date Exists',
    }

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
    std_obj=add_student.objects.all()
    return render(request, 'student/students.html', {'student': std_obj})

def student_view(request):
    
    return render(request, 'student/student-details.html')

def add_student_page(request):
    dep = department_model.objects.all()
    
    if request.method=="POST":
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
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
        s_username=request.POST.get('s_username')
        password=request.POST.get('password')
        
        print(dep_id)
        dept=department_model.objects.get(id=dep_id)
        print(dept)
        
        if custom_user.objects.filter(username=s_username).exists():
            pass
        else:
            std_custom=custom_user.objects.create_user(
                username=s_username,
                password=password,
                user_type='3',
            )
            std_custom.save()
        
            save_std = add_student.objects.create(
                user=std_custom,
                f_name=f_name,
                l_name=l_name,
                std_id=s_username,
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
                department_add=dept,
            )
            save_std.save()
        return redirect('students')
    
    return render(request, 'student/add-student.html',{'departments' : dep})

def del_student(request, std_id):
    del_std=add_student.objects.get(id=std_id)
    del_std.delete()
    messages.success(request, context['delete_message'])
    return redirect('students')

def edit_student(request, std_id):
    get_std = add_student.objects.get(id=std_id)
    return render(request, 'student/edit-student.html', {'student':get_std})

def update_std(request):
    if request.method=="POST":
        std_id=request.POST.get('std_id')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')

        religion=request.POST.get('religion')
        Joining_date=request.POST.get('Joining_date')
        phone=request.POST.get('phone')
        section=request.POST.get('section')

        stdimg=request.FILES.get('img')
        pre_img=request.POST.get('pre_img')

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

        if stdimg == None:
            save_std=add_student(
                id=std_id,
                img=pre_img,
                f_name=f_name,
                l_name=l_name,
                
                gender=gender,
                dob=dob,
                religion=religion,
                Joining_date=Joining_date,
                phone=phone,
                section=section,
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
            )
            save_std.save()
            return redirect('students')
            
        else:
            save_std = add_student(
            id=std_id,
            f_name=f_name,
            l_name=l_name,
                
            gender=gender,
            dob=dob,
            religion=religion,
            Joining_date=Joining_date,
            phone=phone,
            section=section,
            img=stdimg,
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
            )
            save_std.save()
            messages.success(request, context['save_data'])
            return redirect('students')

        

# Tracher
def teachers(request):
    teacher_list=add_teacher_model.objects.all()
    return render(request, 'teacher/teachers.html',{'view_teacher':teacher_list})

def teacher_view(request):
    return render(request, 'teacher/teacher-details.html')

def add_teacher(request):
    if request.method=="POST":
        teacher_name = request.POST.get('teacher_name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        Joining_date = request.POST.get('Joining_date')
        edu_qualify = request.POST.get('edu_qualify')
        experience = request.POST.get('experience')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        t_img = request.FILES.get('t_img')
        
        dep_id = request.POST.get('dep')
        t_username = request.POST.get('t_username')
        t_email = request.POST.get('t_email')
        password = request.POST.get('password')
        
        if custom_user.objects.filter(username=t_username).exists():
            pass
        else:
            add_teacher_user = custom_user.objects.create_user(
                username = t_username,
                email = t_email,
                password = password,
                user_type= '2',
            )
            add_teacher_user.save()
            
            add_teacher_data =add_teacher_model(
                teacher_name = teacher_name,
                gender = gender,
                mobile = mobile,
                Joining_date = Joining_date,
                edu_qualify = edu_qualify,
                experience = experience,
                present_address = present_address,
                permanent_address = permanent_address,
                t_img = t_img,
                user = add_teacher_user,
                dep_obj_add= department_model.objects.get(id=dep_id)
            )
            add_teacher_data.save()
            messages.success(request, context['save_data'])
            return redirect('teachers')
    return render(request, 'teacher/add-teacher.html', {'departments': department_model.objects.all()})

def edit_teacher(request):
    return render(request, 'teacher/edit-teacher.html')



# Department
def departments(request):
    
    std_data=[]
    for department in department_model.objects.all():
        # print(add_student.objects.filter(department_add=department).count())
        std_count=add_student.objects.filter(department_add=department).count()
        teacher_count=add_teacher_model.objects.filter(dep_obj_add=department).count()
        subject_count=subject_model.objects.filter(subject_add_dep=department).count()
        print(add_teacher_model.objects.filter(dep_obj_add=department).count())
        std_data.append(
            {
                "Total_student" : std_count,
                "Total_teacher" : teacher_count,
                "Total_subject" : subject_count,
                "Department_name" : department.department_name,
                "HOD" : department.department_head_name,
                "ID" : department.id,
            }
        )
        context={
            'department_list': std_data,
        }
    return render(request, 'department/departments.html', context)

def add_department(request):

    if request.method=="POST":
        dep_name =request.POST.get('dep_name')
        dep_head =request.POST.get('dep_head')
        if department_model.objects.filter(department_name=dep_name).exists():
            messages.warning(request, context['date_exists'])
            return redirect('add_department')
        else:
            save_dep = department_model(
                department_name=dep_name,
                department_head_name=dep_head,
            )
            save_dep.save()
            messages.success(request, context['save_data'])
            return redirect('departments')
    return render(request, 'department/add-department.html')

def delete_department(request, dep_id):
    del_dep=department_model.objects.get(id=dep_id)
    del_dep.delete()
    messages.success(request, context['delete_message'])
    return redirect('departments')



def edit_department(request, dep_id):
    dep_get=department_model.objects.get(id=dep_id)
    return render(request, 'department/edit-department.html',{'get_dep' : dep_get})


def update_dep(request):
    if request.method=="POST":
        dep_id=request.POST.get('dep_id')
        dep_name=request.POST.get('dep_name')
        hod=request.POST.get('hod')
        save_dep=department_model(
            id=dep_id,
            department_name=dep_name,
            department_head_name=hod,
        )
        save_dep.save()
        messages.success(request, context['update'])
        return redirect('departments')




# Subject

def subjects(request):
    
    return render(request, 'subject/subjects.html', {'subjects': subject_model.objects.all()})

def add_subject(request):
    deppartments = department_model.objects.all()
    
    if request.method=="POST":
        sub_code = request.POST.get('sub_code')
        sub_name = request.POST.get('sub_name')
        dep = request.POST.get('dep')
        dep_inc= department_model.objects.get(id=dep)
        save_subject=subject_model(
            subject_code = sub_code,
            subject_name = sub_name,
            subject_add_dep = dep_inc,
        )
        save_subject.save()
        messages.success(request, context['save_data'])
        return redirect('subjects')
    return render(request, 'subject/add-subject.html',{'departments' : deppartments})

def delete_subject(request, sub_id):
    del_sub=subject_model.objects.get(id=sub_id)
    del_sub.delete()
    messages.success(request, context['delete_message'])
    return redirect('subjects')
    
def edit_subject(request):
    return render(request, 'subject/edit-subject.html')




#Account Management

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
                messages.success(request, context['User_login'])
                return redirect('admin_dashboard')
            elif request.user.user_type=='2':
                messages.success(request, context['User_login'])
                return redirect('teacher_dashboard')
            elif request.user.user_type=='3':
                messages.success(request, context['User_login'])
                return redirect('student_dashboard')
            else:
                messages.error(request, context['pass_wrong'])
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
            messages.success(request, context['acc_succes'])
            return redirect("index")
        else:
            messages.warning(request, context['pass_wrong'])
            return redirect("signupPage")
        
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    messages.success(request, context['logout_message'])
    return redirect("loginPage")
