from django.contrib import admin
from candidateApp.models import candidate_model, student_model
# Register your models here.
admin.site.register(candidate_model)
admin.site.register(student_model)
