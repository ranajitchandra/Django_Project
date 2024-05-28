
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolioApp.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('resume/', resume, name='resume'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('editinfo/<int:info_id>', editinfo, name='editinfo'),
    path('sava_info/', sava_info, name='sava_info'),
    path('editskill/<int:info_id>', editskill, name='editskill'),
    path('sava_skill/', sava_skill, name='sava_skill'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
