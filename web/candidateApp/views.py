from django.shortcuts import render, redirect
from candidateApp.models import candidate_model, student_model
# Create your views here.

def home(request):
    return render(request, 'home.html')

def candidatebtl(request):
    
    candi=candidate_model.objects.all()
    
    get_data={
        'row' : candi
    }
    return render(request, 'candidate_table.html',get_data)

def addcandidate(request):
    
    if request.method=='POST':
        f_name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        jobtitle=request.POST.get('jobtitle')
        linkedin=request.POST.get('linkedin')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        language=request.POST.get('language')
        yoe=request.POST.get('yoe')
        
        candidate_save=candidate_model(
            
            full_name=f_name,
            email=email,
            phone=phone,
            address=address,
            job_title=jobtitle,
            linkedin=linkedin,
            university=university,
            degree=degree,
            language=language,
            yoe=yoe
        )
        candidate_save.save()
        return redirect('candidatebtl')
    
    return render(request, 'add_candidate.html')


def editcandidate(request, id):
    
    obj=candidate_model.objects.get(id=id)
    
    return render(request, 'edit_candidate.html', {'edit_row':obj})

def update_candidate(request):
    if request.method=='POST':
        id=request.POST.get('id')
        f_name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        jobtitle=request.POST.get('jobtitle')
        linkedin=request.POST.get('linkedin')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        language=request.POST.get('language')
        yoe=request.POST.get('yoe')
        
        candidate_save=candidate_model(
            id=id,
            full_name=f_name,
            email=email,
            phone=phone,
            address=address,
            job_title=jobtitle,
            linkedin=linkedin,
            university=university,
            degree=degree,
            language=language,
            yoe=yoe
        )
        candidate_save.save()
        return redirect('candidatebtl')
    
def delete_candidate(request, id):
    
    delete_candidate=candidate_model.objects.get(id=id)
    delete_candidate.delete()
    return redirect('candidatebtl')

def view_candidate(request, c_id):
    
    view_obj=candidate_model.objects.get(id=c_id)
    return render(request, 'candidate_view.html', {'view':view_obj})







def student_table(request):
    std_obj=student_model.objects.all()
    get_obj={
        'row' : std_obj
    }
    return render(request, 'student_tbl.html', get_obj)

def add_stu(request):
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        lavel=request.POST.get('lavel')
        image=request.FILES.get('img')
        
        std_save=student_model(
            name=name,
            roll=roll,
            lavel=lavel,
            std_img=image,
        )
        std_save.save()
        return redirect("student_table")
    
    return render(request, 'add_student.html')


def edit_student(request, myid):
    
    obj=student_model.objects.filter(id=myid)
    
    fatch={
        'std_row':obj
    }
    
    return render(request, 'edit_student.html',fatch)

def update_student(request):
    if request.method=="POST":
        mid=request.POST.get('id')
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        lavel=request.POST.get('lavel')
        image=request.FILES.get('img')
        image2=request.POST.get('preimage')
        
        if image==None:
            stdupdate=student_model(
                id=mid,
                name=name,
                roll=roll,
                lavel=lavel,
                std_img=image2
            )
            stdupdate.save()
            return redirect('student_table')

        else:
            stdupdate=student_model(
                id=mid,
                name=name,
                roll=roll,
                lavel=lavel,
                std_img=image,
            )
            stdupdate.save()
            return redirect('student_table')
            

def delete_student(request, myid):
    
    std_obj=student_model.objects.get(id=myid)
    std_obj.delete()
    return redirect('student_table')
            