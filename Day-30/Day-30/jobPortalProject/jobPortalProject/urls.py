from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobPortalProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signInPage, name = 'signInPage'),
    path('signUpPage/', signUpPage, name = 'signUpPage'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('logoutfn/', logoutfn, name = 'logoutfn'),
    path('profile/', profile, name = 'profile'),
    path('addjobform/', addjobform, name = 'addjobform'),
    path('viewslist/', viewslist, name = 'viewslist'),
    path('profile/editProfilePage/', editProfilePage, name = 'editProfilePage'),
    path('profile/BasicInformation/', BasicInformation, name = 'BasicInformation'),
    path('profile/EducationQualification/', EducationQualification, name = 'EducationQualification'),

    path('changePasswordPage/', changePasswordPage, name = 'changePasswordPage'),
    path('seekerApplyPage/<str:myid>', seekerApplyPage, name = 'seekerApplyPage'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)