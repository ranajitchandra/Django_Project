from django.contrib import admin
from newApp.models import user_info_model, custom_user

# Register your models here.

admin.site.register(user_info_model)
class custom_user_display(admin.ModelAdmin):
    list_display=['username']
admin.site.register(custom_user, custom_user_display)
