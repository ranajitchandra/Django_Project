
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myProject.views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', signinPage,name="signinPage"),
    path('signupPage/', signupPage,name="signupPage"),
    path('dashboardPage/', dashboardPage,name="dashboardPage"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    path('categoryPage/', categoryPage,name="categoryPage"),
    path('categorylist/', categorylist,name="categorylist"),
    path('createTaskPage/', createTaskPage,name="createTaskPage"),
    path('taskList/', taskList,name="taskList"),
    path('editTaskPage/<str:myid>', editTaskPage,name="editTaskPage"),
    path('DeleteTaskPage/<str:myid>', DeleteTaskPage,name="DeleteTaskPage"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
