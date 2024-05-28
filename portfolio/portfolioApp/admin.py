from django.contrib import admin
from portfolioApp.models import personal_info, experience, education, skill

# Register your models here.

admin.site.register(personal_info)
admin.site.register(experience)
admin.site.register(education)
admin.site.register(skill)

