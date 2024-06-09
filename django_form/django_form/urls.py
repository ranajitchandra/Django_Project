
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todo_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage/', signupPage, name="signupPage"),
    path('signinPage/', signinPage, name="signinPage"),
    path('dashboard/', dashboard, name="dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)