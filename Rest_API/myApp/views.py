from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myApp.models import student, teacher, employee
from myApp.serializer import studentSerializer, employee_json_format, teacher_json_format


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework import mixins
from rest_framework import generics


from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        obj = student.objects.all()
        serializer = studentSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def teacher_list(request):
    if request.method=="GET":
        obj=teacher.objects.all()
        teacher_serializer=teacher_json_format(obj, many=True)
        return JsonResponse(teacher_serializer.data, safe=False)
    
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method=="GET":
        obj=employee.objects.all()
        emp_serializer=employee_json_format(obj, many=True)
        return Response(emp_serializer.data)
    elif request.method=="POST":
        emp_serializer=employee_json_format(data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data, status=status.HTTP_201_CREATED)
        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class emp(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_json_format
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class emp_details(generics.ListCreateAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_json_format

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)