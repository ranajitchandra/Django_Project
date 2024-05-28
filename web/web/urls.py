
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from candidateApp.views import delete_student, update_student, home, candidatebtl, addcandidate, editcandidate, update_candidate, delete_candidate, view_candidate, student_table, add_stu, edit_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('candidatebtl/', candidatebtl, name='candidatebtl'),
    path('addcandidate/', addcandidate, name='addcandidate'),
    path('editcandidate/<int:id>', editcandidate, name='editcandidate'),
    path('update_candidate/', update_candidate, name='update_candidate'),
    path('delete_candidate/<int:id>', delete_candidate, name='delete_candidate'),
    path('view_candidate/<int:c_id>', view_candidate, name='view_candidate'),
    path('student_table/', student_table, name='student_table'),
    path('add_stu/', add_stu, name='add_stu'),
    path('edit_student/<int:myid>', edit_student, name='edit_student'),
    path('update_student/', update_student, name='update_student'),
    path('delete_student/<int:myid>', delete_student, name='delete_student'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
