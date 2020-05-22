from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from school.methods import *
from rest_framework import status
from .models import *
import traceback
from . import serializers




class getAlltutorial (APIView) :

    permission_classes=(IsAuthenticated,)
    def get(self,request):
        try :
            all_tutorial = Tutrial.objects.all()
            serializer = serializers.serializer(all_tutorial , many = True)
            return CustomResponse(self, status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)
        except Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class tutorialApi(APIView):
    permission_classes = (IsAuthenticated)
    def get (self, request) :
        try :
            tutorial_id = request.GET['tutorial_id']
            if  Tutrial.objects.all().filter(id =tutorial_id ).exists() :
                temp_tutoril = Tutrial.objects.get(id = tutorial_id)
                serializer = serializers.serializer(temp_tutoril , )
                return CustomResponse( self , status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)

            else :
                return CustomResponse(self, status_code=406, errors=["اموزش مورد نظر وجود ندارد!"], message="", data =serializer.data, status=status.HTTP_200_OK)
        except  Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self,requset) :
        try :
            serializer = serializers.TutorialSerilizer(data = requset.data )
            if  serializer.is_valid() :
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message = "فایل با موفقیت اپلود شد", data="", status=status.HTTP_200_OK)
            else :
                massage = serializer.errors
                return CustomResponse(self, status_code=406, errors = massage, message="", data="", status=status.HTTP_200_OK)

        except  Exception as  e:
                trace_back = traceback.format_exc()
                message = str(e) + ' ' + str(trace_back)
                return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        def delete(self , request):
            try:
                id = request.GET['id']
                if Tutrial.objects.all().filter(id = id).exists():
                    temp_tutorial  = Tutrial.objects.get(id = id)
                else:
                    return CustomResponse(self, status_code=406,message = ["فایل با این ایدی موجود نیست !"] , errors = "", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                    temp_tutorial.delete()
                    return CustomResponse(self, status_code=200, errors="", message="فایل با موفقیت حذف شد", data=[], status=status.HTTP_200_OK)
            except Exception as e:
                trace_back = traceback.format_exc()
                message = str(e) + ' ' + str(trace_back)
                return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put (self, request) :
            try :
                id = request.GET['id']
                if Tutrial.objects.all().filter(id = id).exists():
                    temp_tutorial = Tutrial.objects.get(id = id)
                else:
                    return CustomResponse(self, status_code=406, errors=["فایل با این ایدی موجود نیست"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                    serializer = serializers.NewsSerializer(Tutrial,data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors="", message="فایل با موفقیت اپدیت شد", data=[], status=status.HTTP_200_OK)
            except Exception as e :
                trace_back = traceback.format_exc()
                message = str(e) + ' ' + str(trace_back)
                return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


