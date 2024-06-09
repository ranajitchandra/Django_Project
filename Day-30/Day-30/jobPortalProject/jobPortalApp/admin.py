from django.contrib import admin
from jobPortalApp.models import *

# Register your models here.
class customUserDisplay(admin.ModelAdmin):

    list_display = ['username', 'gender', 'user_type']



admin.site.register(customUserModel,customUserDisplay)

class JobModelDisplay(admin.ModelAdmin):

    list_display = ["job_titel","company_name","address","salary"]

    search_fields = ["job_titel","company_name"]

    
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [("job_titel","company_name"),("address","job_desciption","company_desciption")]
            }
        ),
        (
            "Advanced Options",
            {
                "classes":["collapse"],
                "fields":["qualification","salary","created_by"]
            }
        )
    ]

admin.site.register(job_model,JobModelDisplay)

class jobApplyModelDisplay(admin.ModelAdmin):

    list_display = ["applicant","job","skills","qualification"]

    search_fields = ["applicant","job"]


admin.site.register(jobApplyModel,jobApplyModelDisplay)

    

admin.site.register(JobRecruiterProfile)
admin.site.register(JobSeekerProfile)