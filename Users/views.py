from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
import traceback
from . import serializers


class ImageApi(APIView):
    permission_classes=(IsAuthenticated,)
    #################################### get method for find specific user images
    def get(self , request):
        try:
            user_id = request.GET['user_id']
            image_list = []
            if Images.objects.all().filter(user_id = user_id).exists():
                image_list = Images.objects.all().filter(user_id = user_id)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
            serializer = serializers.ImageSerilizer(image_list , many=True)
            return Response({"status_code":"200" , "error":"", "data": serializer.data , "message":""},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" ,"error":message,"data": "" ,"message":""},)
    ######################################## post method for upload image
    def post(self , request):
        try:
            serializer = serializers.ImageSerilizer(data = request.data)
            user_id = request.data['user_id']
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code":"200" , "error": "","data": str(serializer.instance.image) ,"message":"Image Uploaded Success"},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": message ,"data":"","message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)


class UserApi(APIView):
    permission_classes=(IsAuthenticated,)
    ######################### get method for find specific user
    def get(self ,request):
        try:
            id = request.GET['id']
            if User.objects.all().filter(id = id).exists():
                temp_user = User.objects.get(id = id)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
            serializer = serializers.UserSerializer(temp_user)
            return Response({"status_code":"200" , "error":"", "data": serializer.data , "message":""},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" ,"error":message,"data": "" ,"message":""},)

    ######################### put method for edit specific user
    def put(self , request):
        try:
            id = request.GET['id']
            if User.objects.all().filter(id = id).exists():
                temp_user = User.objects.get(id = id)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
            serializer = serializers.UserSerializer(temp_user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code":"200" , "error": "","data":"","message":"User Updated Success"},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": message ,"data":"","message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)

    def delete(self , request):
        try:
            id = request.GET['id']
            if User.objects.all().filter(id = id).exists():
                User.objects.get(id = id).delete()
                return Response({"status_code":"200" , "error": "","data":"","message":"User Deleted Success"},)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)

class UserDocApi(APIView):
    permission_classes=(IsAuthenticated,)
    ############################# method for get specific user doc
    def get(self ,request):
        try:
            user_id = request.GET['user_id']
            if userDoc.objects.all().filter(user_id = user_id).exists():
                temp_userDoc = userDoc.objects.get(user_id = user_id)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
            serializer = serializers.UserDocSerializer(temp_userDoc)
            return Response({"status_code":"200" , "error":"", "data": serializer.data , "message":""},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)
    ############################### method for edit specific user doc
    def put(self , request):
        try:
            user_id = request.GET['user_id']
            if userDoc.objects.all().filter(user_id = user_id).exists():
                temp_userDoc = userDoc.objects.get(user_id = user_id)
            else:
                return Response({"status_code":"400" , "error": "object does not exist for this user","data":"","message":""},)
            serializer = serializers.UserDocSerializer(temp_userDoc, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code":"200" , "error": "","data":"","message":"User Updated Success"},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": "","data":message,"message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)

class registerUser(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            serializer = serializers.UserRegisterSerializer(data = request.data)
            if serializer.is_valid():
                new_user = User()

                new_user.username = serializer.instance.nationalCode
                new_user.first_name = serializer.instance.nationalCode
                new_user.last_name = serializer.instance.nationalCode
                new_user.email = serializer.instance.nationalCode
                new_user.set_password(serializer.instance.nationalCode)
                new_user.save()

                new_userDoc = userDoc(user_id = new_user.id,religon=serializer.instance.religon,userPhoto=serializer.instance.userPhoto,
                userNationalCardPhoto=serializer.instance.userNationalCardPhoto,userIdCardPhoto=serializer.instance.userIdCardPhoto,
                user_pNum=serializer.instance.user_pNum,home_pNum=serializer.instance.home_pNum,address=serializer.instance.address,
                zipcode=,personalCode=,nationalCode=,father_nationalCode=,father_name=,father_pNum=,father_jobName=,father_jobName=,
                father_job_pNum=,mother_nationalCode=,mother_name=,mother_pNum=,mother_jobName=,mother_jobAddress=,mother_job_pNum=,
                citizen_Num=,date_of_birth=,place_of_birth=,role=,citizen=,gender=,section=)
                new_userDoc.save()

                return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Created"},status.HTTP_200_OK)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": "","data":message,"message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" ,"error":message,"data": "" ,"message":""},)
