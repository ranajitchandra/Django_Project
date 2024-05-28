
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from SchoolApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('index', index, name='index'),
    
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    
    path('students/', students, name='students'),
    path('student_view/', student_view, name='student_view'),
    path('add_student/', add_student_page, name='add_student'),
    path('edit_student/', edit_student, name='edit_student'),
    
    path('teachers/', teachers, name='teachers'),
    path('teacher_view/', teacher_view, name='teacher_view'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('edit_teacher/', edit_teacher, name='edit_teacher'),
    
    path('departments/', departments, name='departments'),
    path('add_department/', add_department, name='add_department'),
    path('edit_department/', edit_department, name='edit_department'),
    
    
    path('subjects/', subjects, name='subjects'),
    path('add_subject/', add_subject, name='add_subject'),
    path('edit_subject/', edit_subject, name='edit_subject'),
    
    path('fees_collections/', fees_collections, name='fees_collections'),
    path('expenses/', expenses, name='expenses'),
    path('salary/', salary, name='salary'),
    path('add_fees_collection/', add_fees_collection, name='add_fees_collection'),
    path('add_expenses/', add_expenses, name='add_expenses'),
    path('add_salary/', add_salary, name='add_salary'),
    path('holiday/', holiday, name='holiday'),
    path('fees/', fees, name='fees'),
    path('exam/', exam, name='exam'),
    path('event/', event, name='event'),
    path('time_table/', time_table, name='time_table'),
    path('library/', library, name='library'),
    
    
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('logout_page/', logout_page, name='logout_page'),
]
