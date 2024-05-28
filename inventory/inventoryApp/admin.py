from django.contrib import admin
from inventoryApp.models import custom_user, add_data

# Register your models here.
class custom_user_display(admin.ModelAdmin):
    list_dispaly=['display_name', 'username']

admin.site.register(custom_user, custom_user_display)
admin.site.register(add_data)