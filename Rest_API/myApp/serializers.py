from django.contrib.auth.models import Group, User
from rest_framework import serializers

from myApp.models import student


class student_serializer(serializers.Serializer):
    name=serializers.CharField()
    dep=serializers.CharField()
    email=serializers.EmailField()
    
    def create(self, validated_data):
        return student.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dep = validated_data.get('dep', instance.dep)
        instance.email = validated_data.get('email', instance.email)
        
        instance.save()
        return instance