from django.contrib import admin
from todo_list.models import *
# Register your models here.

class custom_user_display(admin.ModelAdmin):
    list_display = ['username', 'email', 'city', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'city']
    
    fieldsets = [
        ('This is my Title', {'fields':['username', 'email', 'password']}),
        ('Advance Option', {'classes' : ['collapse'], 'fields': ['city', 'profile_pic']})
    ]

admin.site.register(Custom_user,custom_user_display)