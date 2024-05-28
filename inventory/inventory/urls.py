
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inventoryApp.views import signup_Page, signin_Page, view_data_page, logout_page, homepage, add_data_page, delete_data, edit_data_page, update_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin_Page, name='signin_Page'),
    path('signup_Page/', signup_Page, name='signup_Page'),
    path('view_data_page/', view_data_page, name='view_data_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('homepage/', homepage, name='homepage'),
    path('add_data_page/', add_data_page, name='add_data_page'),
    path('delete_data/<int:delid>', delete_data, name='delete_data'),
    path('edit_data_page/<int:editid>', edit_data_page, name='edit_data_page'),
    path('update_data/', update_data, name='update_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
