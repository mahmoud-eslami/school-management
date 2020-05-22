from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
import traceback
from . import serializers




class getAlltutorial ()
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        try :
            all_tutorial = Tutrial.objects.all()
            # serializer = serializers.serializer(all_tutorial , many = True)
            return CustomResponse(self, status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)
        except Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class tutorialApi(APIView):
    permission_classes = (IsAuthenticated)
    def get (seflf, request) :
        try :
        tutorial_id = request.GET['tutorial_id']
        if  Tutrial.objects.all().filter(id =tutorial_id ).exists() :
            temp_tutoril = Tutrial.objects.get(id = tutorial_id)
            #serializer = serializers.serializer(temp_tutoril , )
            return CustomResponse(self, status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)

        else :
            return CustomResponse(self, status_code=406, errors=["اموزش مورد نظر وجود ندارد!"], message="", data =serializer.data, status=status.HTTP_200_OK)  
        except  Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self,requset) :
        try : 
            use_id =Tutrial.objects.   