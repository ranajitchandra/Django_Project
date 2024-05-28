from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', base, name='base'),
    path('user_table/', user_table, name='user_table'),
    path('add_user/', add_user, name='add_user'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user'),
    path('edit_user/<int:user_id>', edit_user, name='edit_user'),
    path('index_page/', index_page, name='index_page'),
    path('resume_page/', resume_page, name='resume_page'),
    path('project_page/', project_page, name='project_page'),
    path('contact_page/', contact_page, name='contact_page'),
    path('signup/', signup, name='signup'),
    path('', signin, name='signin'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
