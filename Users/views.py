from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *

class registerUser(APIView):
    def post(self, request):
        #try:
            # new user created
            new_user = User()
            # new profile created for new user
            new_profile = userProfile()
            # new doc created for new user
            new_doc = userDoc()
            # get user info
            new_user.username = request.data['username']
            new_user.email = request.data['email']
            new_user.first_name = request.data['first_name']
            new_user.last_name = request.data['last_name']
            password = request.data['password']
            new_user.set_password(password)
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
            citizen_num = request.data['citizen_num']
            new_doc.citizen_Num = citizen_num
            new_doc.zipCode = request.data['zipcode']
            new_doc.date_of_birth = request.data['date_birth']
            new_doc.place_of_birth = request.data['place_birth']
            new_doc.save()
            return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Created"},status.HTTP_200_OK)
        #except:
            #return Response({"status_code":"500" ,"error":"Field Error","data": "" ,"message":""},)

class findUserById(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class findUserByUsername(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class findUserProfileByUsername(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class findUserDocByUsername(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUser(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUserProfile(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUserDoc(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class deleteUser(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            user_id = request.data['user_id']
            User.objects.all().filter(id = user_id).delete()
            return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Deleted Success"},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" ,"error":"Internal Server Error","data": "" ,"message":""},)


class getAllUser(APIView):
    #permission_classes=(IsAuthenticated,)
    def get(self, request):
        try:
            temp_users = User.objects.all()
            json_data = []
            for item in temp_users:
                # TODO: add serializer for serialize data
                json_data.append({
                    'id':item.id,
                    'username':item.username,
                    'name':item.first_name,
                    'lname':item.last_name,
                    'email':item.email,
                    'date_joined':item.date_joined,})
            return Response({"status_code":"200" ,"error":"","data": json_data ,"message":""},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" ,"error":"Internal Server Error","data": "" ,"message":""},)
