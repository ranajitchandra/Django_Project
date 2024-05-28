
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('add_jobPage/', add_jobPage, name='add_jobPage'),
    path('view_job/', view_job, name='view_job'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('applied_job/', applied_job, name='applied_job'),
    path('delete_data/<int:job_id>', delete_data, name='delete_data'),
    path('basic_info/', basic_info, name='basic_info'),
    path('education/', education, name='education'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change_pass/', change_pass, name='change_pass'),
    path('update_pass/', update_pass, name='update_pass'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
