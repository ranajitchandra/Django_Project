from django.contrib import admin
from myApp.models import student, teacher, employee

# Register your models here.

admin.site.register(student)
admin.site.register(teacher)
admin.site.register(employee)
