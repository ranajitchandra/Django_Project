from rest_framework import serializers

from myApp.models import student, teacher, employee

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id', 'name', 'dep', 'email']
        
        
        
class teacher_json_format(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = ['id', 'name', 'address', 'salary']
        
class employee_json_format(serializers.ModelSerializer):
    class Meta:
        model = employee
        exclude = []