from django.contrib import admin

from custom_userApp.models import Custom_User_Model

# Register your models here.
class user_display(admin.ModelAdmin):
    list_display=['User_name', 'User_password']
admin.site.register(Custom_User_Model, user_display)
