from django.contrib import admin

from jobApp.models import *
# Register your models here.

class Custom_user_display(admin.ModelAdmin):
    list_display=['username', 'display_name']
admin.site.register(Custom_User, Custom_user_display)
admin.site.register(add_job)
admin.site.register(jobseeker_profile)
admin.site.register(jobrecruiter_profile)
admin.site.register(educationModel)