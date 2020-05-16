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
            # new user created
            new_user = User()
            # new profile created for new user
            new_profile = userProfile()
            # new doc created for new user
            new_doc = userDoc()
            # get user info
            #################################
            new_user.username = request.data['username']
            #################################
            new_user.email = request.data['email']
            new_user.first_name = request.data['first_name']
            new_user.last_name = request.data['last_name']
            password = request.data['password']
            #################################
            new_user.set_password(password)
            #################################
            new_user.save()
            # get user profile info
            new_profile.user = new_user
            role = request.data['role'] # 1 to 4
            new_profile.role = role
            new_profile.save()
            # get user doc info
            new_doc.user = new_user
            new_doc.gender = request.data['gender'] # 1 or 0
            new_doc.section = request.data['section'] # 1 to 5
            new_doc.address = request.data['address']
            # check user role
            if role == '4':
                personal_code = ''
            else:
                personal_code = request.data['personal_code']
            new_doc.personalCode = personal_code
            new_doc.nationalCode = request.data['national_code']
            new_doc.home_pNum = request.data['home_phone_num']
            new_doc.user_pNum = request.data['user_phone_num']
            new_doc.father_name = request.data['father_name']
            new_doc.father_nationalCode = request.data['father_national_code']
            new_doc.father_pNum = request.data['father_phone_num']
            new_doc.father_jobName = request.data['father_job_name']
            new_doc.father_jobAddress = request.data['father_job_address']
            new_doc.father_job_pNum = request.data['father_job_phone_num']
            new_doc.userPhoto = request.data['user_photo']
            new_doc.nationalCardPhoto = request.data['national_card_photo']
            new_doc.mother_name = request.data['mother_name']
            new_doc.mother_jobName = request.data['mother_job_name']
            new_doc.mother_jobAddress = request.data['mother_job_address']
            new_doc.mother_job_pNum = request.data['mother_job_phone_num']
            new_doc.mother_nationalCode = request.data['mother_national_code']
            new_doc.mother_pNum = request.data['mother_pNum']
            new_doc.citizen = request.data['citizen'] # 1 or 0
            new_doc.citizen_Num = request.data['citizen_num']
            new_doc.zipCode = request.data['zipcode']
            new_doc.date_of_birth = request.data['date_birth']
            new_doc.place_of_birth = request.data['place_birth']
            new_doc.save()
            return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Created"},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" ,"error":message,"data": "" ,"message":""},)
