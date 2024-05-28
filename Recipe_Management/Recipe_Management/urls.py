
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recipeApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin_page, name='signin_page'),
    path('signup_page/', signup_page, name='signup_page'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('view_recipe/', view_recipe, name='view_recipe'),
    path('base/', base, name='base'),
    path('logout_user/', logout_user, name='logout_user'),
    path('datele_recipe/<int:recipe_id>', datele_recipe, name='datele_recipe'),
    path('edit_recipe/<int:recipe_id>', edit_recipe, name='edit_recipe'),
    path('update_recipe/', update_recipe, name='update_recipe'),
    path('user_profile/', user_profile, name='user_profile'),
    path('home_page/', home_page, name='home_page'),
    path('view2_recipe/', view2_recipe, name='view2_recipe'),
    path('chef_profile_page/', chef_profile_page, name='chef_profile_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
