from django.shortcuts import render
from school.methods import *
from school.validators import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from . import serializers
from school.methods import  *
from school.validators import  *
from .models import *
import traceback

class GetAllClasses(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self , request):
        try:
            temp_classes = Classes.objects.all()
            serializer = serializers.ClassSerializer(temp_classes, many=True)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllUserClasses(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self , request):
        try:
            temp_userClass = UserClass.objects.all()
            serializer = serializers.UserClassSerializer(temp_userClass,many=True)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClassesApi(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self , request):
        try:
            class_id = request.GET['class_id']
            if Classes.objects.filter(id = class_id).exists():
                temp_class = Classes.objects.get(id = class_id)
                serializer = serializers.ClassSerializer(temp_class)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="کلاس مورد نظر موجود نیست .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:    
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def post(self , request):
        try:
            serializer = serializers.ClassSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message="کلاس با موفقیت ایجاد شد .", data="", status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:    
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def delete(self , request):
        try:
            class_id = request.GET['class_id']
            if Classes.objects.filter(id = class_id).exists():
                Classes.objects.filter(id = class_id).delete()
                return CustomResponse(self, status_code=200, errors=[], message="کلاس با موفقیت حذف شد .", data="", status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="کلاس مورد نظر موجود نیست .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:    
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def put(self , request):
        try:
            class_id = request.GET['class_id']
            if Classes.objects.filter(id = class_id).exists():
                temp_class = Classes.objects.get(id = class_id)
                serializer = serializers.ClassSerializer(temp_class , request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors=[], message="اطلاعات کلاس با موفقیت بروزرسانی شد .", data="", status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="کلاس مورد نظر موجود نیست .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:    
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)