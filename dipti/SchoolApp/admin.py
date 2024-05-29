from django.contrib import admin
from SchoolApp.models import *
# Register your models here.

class customUser_display(admin.ModelAdmin):
    list_display=['username', 'email', 'user_type']
    search_fields = ['username', 'email', 'user_type']
    fieldsets = [
      ('Address info', {
          'fields': ['username', 'email', 'user_type', 'image']
      }),
   ]
admin.site.register(custom_user, customUser_display)




class department_view(admin.ModelAdmin):
    list_display = ['department_name', 'create_date_at','update_date_at']
    search_fields = ['department_name']
    fieldsets =[
        ('Department', {'fields': ['department_name', 'department_head_name']})
    ]
    
admin.site.register(department_model,department_view)
admin.site.register(season)
admin.site.register(add_student)
admin.site.register(add_teacher_model)
