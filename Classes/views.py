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

class ClassesApi(APIView):
    pass
