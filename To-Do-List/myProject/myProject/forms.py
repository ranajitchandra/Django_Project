from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from myApp.models import *
from django import forms



class myUserCreationForm(UserCreationForm):

     class Meta:

        model = customUser
        
        fields = UserCreationForm.Meta.fields + ('city', 'profile_pic','user_type',"email","first_name","last_name")

        
class myAuthenticationForm(AuthenticationForm):

    class Meta:

        model = customUser

        fields = ("username","password")

class CategoryForm(forms.ModelForm):

    class Meta:
        
        model = CategoryModel

        fields = ["CategoryName"]

class CreateTaskForm(forms.ModelForm):

    class Meta:
        
        model = TaskModel

        fields=("priority","TaskName","description","due_date","status","completed_date")

        widgets = {

            'due_date': forms.DateInput(attrs={'type': 'date','class':'form-group input'}),

            'completed_date': forms.DateInput(attrs={'type': 'date','class':'form-group input'}),
            
            'description': forms.Textarea(attrs={'type': 'date','class':'form-group input'}),
        }

        labels={
            "priority":"Please enter priority",
            "TaskName":"Task Name:",
            "description":"Enter Description:",
        }

        




