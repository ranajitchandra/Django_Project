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
        
        widgets = {

            'CategoryName': forms.TextInput(attrs={'type': 'text','class':'form-control input'})
        }
        labels={
            "CategoryName":"Category Name"
            
        }

class CreateTaskForm(forms.ModelForm):

    class Meta:
        
        model = TaskModel

        fields=("category","priority","TaskName","description","due_date","completed_date")

        widgets = {

            'category': forms.Select(attrs={'class':'form-control input'}),
            'priority': forms.Select(attrs={'class':'form-control input'}),
            'TaskName': forms.TextInput(attrs={'type': 'text','class':'form-control input'}),
            'description': forms.Textarea(attrs={'class':'form-control input'}),
            'due_date': forms.DateInput(attrs={'type': 'date','class':'form-control input'}),
            'completed_date': forms.DateInput(attrs={'type': 'date','class':'form-control input'}),

        }

        labels={
            "priority":"Please enter priority",
            "TaskName":"Task Name:",
            "description":"Enter Description:",
        }

        




