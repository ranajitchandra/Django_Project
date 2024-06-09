from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from todo_list.models import *
from django import forms

class myUserCreationForm(UserCreationForm):
    
    class Meta:
        model = Custom_user
        fields = UserCreationForm.Meta.fields + ('city', 'user_type', 'profile_pic', 'email', 'first_name', 'last_name')
        
class myAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = Custom_user
        fields = ('username', 'password')