
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', student_list, name='student_list'),
    path('teacher_list/', teacher_list, name='teacher_list'),
    path('emp/', emp.as_view(), name='employee_list'),
    path('emp_details/<int:pk>/', emp_details.as_view(), name='emp_details'),
]
