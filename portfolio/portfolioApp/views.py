from django.shortcuts import render, redirect
from portfolioApp.models import *

# Create your views here.

def base(request):

    return render(request, 'base.html')

def home(request):

    return render(request, 'index.html')

def about(request):

    personal=personal_info.objects.all()
    skills=skill.objects.all()
    data_dict={
        'row' : personal,
        'skill' : skills,
    }
    return render(request, 'about.html', data_dict)

def editinfo(request, info_id):
    per_info=personal_info.objects.get(id=info_id)
    return render(request, 'editinfo_page.html', { 'row_info' : per_info})

def sava_info(request):
    if request.method=="POST":
        info_id=request.POST.get('info_id')
        info_name=request.POST.get('name')
        info_address=request.POST.get('address')
        info_occupation=request.POST.get('occupation')
        info_phone=request.POST.get('phone')
        info_email=request.POST.get('email')
        info_degree=request.POST.get('degree')
        info_summary=request.POST.get('summary')
        info_city=request.POST.get('city')
        info_website=request.POST.get('website')
        info_title=request.POST.get('title')
        info_img_text=request.POST.get('img_text')
        info_img=request.FILES.get('img')
        
       
        if info_img==None:
            save_data=personal_info(
                id=info_id,
                name=info_name,
                address=info_address,
                occupation=info_occupation,
                phone=info_phone,
                email=info_email,
                degree=info_degree,
                summary=info_summary,
                city=info_city,
                website=info_website,
                title=info_title,
                img=info_img_text,
            )
            save_data.save()
            return redirect(about)
        else:
            save_data=personal_info(
                id=info_id,
                name=info_name,
                address=info_address,
                occupation=info_occupation,
                phone=info_phone,
                email=info_email,
                degree=info_degree,
                summary=info_summary,
                city=info_city,
                website=info_website,
                title=info_title,
                img=info_img,
            )
            save_data.save()
            return redirect(about)

def editskill(request, info_id):
    per_skill=skill.objects.get(id=info_id)
    return render(request, 'editskill_page.html', { 'row_skill' : per_skill})

def sava_skill(request):
    if request.method=="POST":
        skill_id=request.POST.get('skill_id')
        skill_html=request.POST.get('s_html')
        skill_css=request.POST.get('s_css')
        skill_js=request.POST.get('s_js')
        skill_python=request.POST.get('s_python')
        skill_php=request.POST.get('s_php')
        skill_sql=request.POST.get('s_sql')
        

        save_data=skill(
                id=skill_id,
                s_html=skill_html,
                s_css=skill_css,
                s_js=skill_js,
                s_python=skill_python,
                s_php=skill_php,
                s_sql=skill_sql,
                
            )
        save_data.save()
        return redirect(about)


def resume(request):
    resume_edu=education.objects.all()
    
    resume_experience=experience.objects.all()

    resume_data={
        'edu' : resume_edu,
        'experience' : resume_experience,
    }

    return render(request, 'resume.html', resume_data)

def portfolio(request):

    return render(request, 'portfolio.html')

def contact(request):

    return render(request, 'contact.html')

