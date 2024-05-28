from django.contrib import admin

from recipeApp.models import *

# Register your models here.
class custom_user_display(admin.ModelAdmin):
    list_display=['username', 'country']
admin.site.register(custom_user, custom_user_display)
admin.site.register(add_recipe_model)
admin.site.register(chef_profile)
admin.site.register(viewer_profile)
