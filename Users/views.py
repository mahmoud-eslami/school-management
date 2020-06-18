from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
import traceback
from . import serializers
from school.methods import *


class ChangePassInProfile(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self , request):
        try:
            user_id = request.user.id
            temp_user = MyUser.objects.get(id = user_id)
            serializer = serializers.ChangePasswordInProfileSerilizer(data = request.data)
            if serializer.is_valid():
                old_password = serializer.data.get('old_password')
                new_password = serializer.data.get('new_password')
                user_password = temp_user.password
                if temp_user.check_password(old_password):
                    temp_user.set_password(new_password)
                    temp_user.save()
                    return CustomResponse(self, status_code=200, errors=["رمز عبور با موفقیت تغییر کرد ."], message="", data="", status=status.HTTP_200_OK)
                else:
                    return CustomResponse(self, status_code=406, errors=["رمز عبور وارد شده با رمز عبور قبلی برابر نیست."], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status = status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateUserAndUserDoc(APIView):
    permission_classes=(IsAuthenticated,)
    def put(self , request):
        try:
            role = request.user.role
            if role == '4' and role == '3':
                return CustomResponse(self,status_code=403,errors=["شما دسترسی به این بخش را ندارید"],message="", data="",status=status.HTTP_403_FORBIDDEN)
            else:
                user_id = request.GET['user_id']
                if MyUser.objects.all().filter(id = user_id).exists():
                    temp_user = MyUser.objects.get(id = user_id)
                    temp_userDoc = userDoc.objects.get(user_id = user_id)
                else:
                    return CustomResponse(self, status_code=406, errors=["کاربری با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                user_serializer = serializers.UserSerializer(temp_user, data=request.data)
                userDoc_serializer = serializers.UserDocSerializer(temp_userDoc, data=request.data)
                if user_serializer.is_valid():
                    if userDoc_serializer.is_valid():
                        user_serializer.save()
                        userDoc_serializer.save()
                        temp_user.username = userDoc_serializer.data.get('nationalCode')
                        temp_user.save()
                        return CustomResponse(self, status_code=200, errors=[], message="اطلاعات کاربر بروزرسانی شد", data="", status=status.HTTP_200_OK)
                    else:
                        message = userDoc_serializer.errors
                        return CustomResponse(self, status_code=406, errors=message, message="", data="", status = status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    message = user_serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status = status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllUserInfo(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self , request):
        try:
            role = request.user.role
            if role == '4':
                return CustomResponse(self,status_code=403,errors=["شما دسترسی به این بخش را ندارید"],message="", data="",status=status.HTTP_403_FORBIDDEN)
            else:
                temp_users = MyUser.objects.all()
                data = []
                #Append our Custom data in a list to send in response
                for user in temp_users:
                    user_userDoc = userDoc.objects.get(user_id = user.id)
                    data.append({
                        'id':user.id,
                        'first_name':user.first_name,
                        'last_name':user.last_name,
                        'nationalCode':user_userDoc.nationalCode,
                        'role':user.role,
                        'section':user_userDoc.section,
                    })
                return CustomResponse(self, status_code=200, errors=[], message="", data=data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class userProfileApi(APIView):
    permission_classes=(IsAuthenticated,)
    #################################### get method for find specific user profile
    def get(self , request):
        try:
            user_id = request.GET['user_id']
            if MyUser.objects.all().filter(id = user_id).exists():
                temp_user = MyUser.objects.get(id = user_id)
                temp_userDoc = userDoc.objects.get(user_id = user_id)
                data = []
                data.append({
                    'first_name':temp_user.first_name,
                    'userPhoto':temp_userDoc.userPhoto,
                    'role':temp_user.role,
                    'last_name':temp_user.last_name,
                    'id':temp_user.id,
                })
                return CustomResponse(self, status_code=200, errors=[], message="", data=data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربر با این ایدی وجود ندارد"],
                message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImageApi(APIView):
    permission_classes=(IsAuthenticated,)
    #################################### get method for find specific user images
    def get(self , request):
        try:
            user_id = request.user.id
            image_list = []
            if Images.objects.all().filter(user_id = user_id).exists():
                image_list = Images.objects.all().filter(user_id = user_id)
            else:
                return CustomResponse(self, status_code=406, errors=["عکسی توسط این کاربر ثبت نشده."],
                message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.ImageSerilizer(image_list , many=True)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    ######################################## post method for upload image
    def post(self , request):
        try:
            serializer = serializers.ImageSerilizer(data = request.data)
            user_id = request.user.id
            if MyUser.objects.all().filter(id = user_id).exists():
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors=[], message="عکس با موفقیت اپلود شد", data=str(serializer.instance.image), status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status = status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربری با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserApi(APIView):
    permission_classes=(IsAuthenticated,)
    ######################### get method for find specific user
    def get(self ,request):
        try:
            user_id = request.GET['user_id']
            if MyUser.objects.all().filter(id = user_id).exists():
                temp_user = MyUser.objects.get(id = user_id)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربری با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.UserSerializer(temp_user)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ######################### put method for edit specific user
    def put(self , request):
        try:
            user_id = request.GET['user_id']
            if MyUser.objects.all().filter(id = user_id).exists():
                temp_user = MyUser.objects.get(id = user_id)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربری با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.UserSerializer(temp_user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message="اطلاعات کاربر بروزرسانی شد", data="", status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status = status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self , request):
        try:
            user_id = request.GET['user_id']
            if MyUser.objects.all().filter(id = user_id).exists():
                MyUser.objects.get(id = user_id).delete()
                return CustomResponse(self, status_code=200, errors=[], message="کاربر با موفقیت حذف شد", data="", status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربر با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDocApi(APIView):
    permission_classes=(IsAuthenticated,)
    ############################# method for get specific user doc
    def get(self ,request):
        try:
            user_id = request.GET['user_id']
            if userDoc.objects.all().filter(user_id = user_id).exists():
                temp_userDoc = userDoc.objects.get(user_id = user_id)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربر با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.UserDocSerializer(temp_userDoc)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    ############################### method for edit specific user doc
    def put(self , request):
        try:
            user_id = request.GET['user_id']
            if userDoc.objects.all().filter(user_id = user_id).exists():
                temp_userDoc = userDoc.objects.get(user_id = user_id)
            else:
                return CustomResponse(self, status_code=406, errors=["کاربر با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.UserDocSerializer(temp_userDoc, request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message="پرونده با موفقیت بروزرسانی شد", data="", status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class registerUserApi(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            serializer = serializers.UserRegisterSerializer(data = request.data)
            if serializer.is_valid():
                new_user = MyUser()

                new_user.username = serializer.data.get('nationalCode')
                new_user.first_name = serializer.data.get('first_name')
                new_user.last_name = serializer.data.get('last_name')
                new_user.email = serializer.data.get('email')
                new_user.role = serializer.data.get('role')
                new_user.set_password(serializer.data.get('nationalCode'))
                new_user.save()

                new_userDoc = userDoc(user_id = new_user.id,religion=serializer.data.get('religion'),userPhoto=serializer.data.get('userPhoto'),
                userNationalCardPhoto=serializer.data.get('userNationalCardPhoto'),userIdCardPhoto=serializer.data.get('userIdCardPhoto'),
                user_pNum=serializer.data.get('user_pNum'),home_pNum=serializer.data.get('home_pNum'),address=serializer.data.get('address'),
                zipCode=serializer.data.get('zipCode'),personalCode=serializer.data.get('personalCode'),nationalCode=serializer.data.get('nationalCode'),
                father_nationalCode=serializer.data.get('father_nationalCode'),father_name=serializer.data.get('father_name'),father_pNum=serializer.data.get('father_pNum'),
                father_jobName=serializer.data.get('father_jobName'),father_jobAddress=serializer.data.get('father_jobAddress'),father_job_pNum=serializer.data.get('father_job_pNum'),
                father_job_postalCode=serializer.data.get('father_job_postalCode'),
                mother_nationalCode=serializer.data.get('mother_nationalCode'),mother_name=serializer.data.get('mother_name'),mother_pNum=serializer.data.get('mother_pNum'),
                mother_job_postalCode=serializer.data.get('mother_job_postalCode'),
                mother_jobName=serializer.data.get('mother_jobName'),mother_jobAddress=serializer.data.get('mother_jobAddress'),mother_job_pNum=serializer.data.get('mother_job_pNum'),
                citizen_Num=serializer.data.get('citizen_Num'),date_of_birth=serializer.data.get('date_of_birth'),place_of_birth=serializer.data.get('place_of_birth'),
                citizen=serializer.data.get('citizen'),gender=serializer.data.get('gender'),section=serializer.data.get('section'))
                new_userDoc.save()

                return CustomResponse(self, status_code=200, errors=[], message="",
                data={"user_id":str(new_user.id),"username":"کلمه کاربری برابر کد ملی","password":"رمز عبور برابر کد ملی",}, status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
