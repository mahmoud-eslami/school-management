from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *

class registerUser(APIView):
    def post(self, request):
        try:
            # get user info
            username = request.data['username']
            email = request.data['email']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            password = request.data['password']
            # get user profile info
            role = request.data['role'] # 1 to 4
            # get user doc info
            gender = request.data['gender'] # 1 or 0
            section = request.data['section'] # 1 to 5
            address = request.data['address']
            personal_code = request.data['personal_code']
            national_code = request.data['national_code']
            father_name = request.data['father_name']
            father_national_code = request.data['father_national_code']
            father_phone_num = request.data['father_phone_num']
            user_photo = request.data['user_photo']
            national_card_photo = request.data['national_card_photo']
            mother_name = request.data['mother_name']
            citizen = request.data['citizen'] # 1 or 0
            citizen_num = request.data['citizen_num']
            zipcode = request.data['zipcode']
            date_birth = request.data['date_birth']
            place_birth = request.data['place_birth']
            # new user created
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.save()
            # new profile created for new user
            new_profile = userProfile()
            new_profile.user = new_user
            new_profile.role = role
            new_profile.save()
            # new doc created for new user
            new_doc = userDoc()
            new_doc.user = new_user
            new_doc.gender = gender
            new_doc.section = section
            new_doc.address = address
            new_doc.personalCode = personal_code
            new_doc.nationalCode = national_code
            new_doc.father_name = father_name
            new_doc.father_nationalCode = father_national_code
            new_doc.userPhoto = user_photo
            new_doc.nationalCardPhoto = national_card_photo
            new_doc.mother_name = mother_name
            new_doc.citizen = citizen
            new_doc.citizen_Num = citizen_num
            new_doc.zipCode = zipcode
            new_doc.date_of_birth = date_birth
            new_doc.place_of_birth = place_birth
            new_doc.save()
            return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Created"},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" ,"error":"Wrong Field Error","data": "" ,"message":""},)

class findUserById(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class findUserByUsername(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUser(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUserProfile(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class editSpecificUserDoc(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            pass
        except:
            pass

class deleteUser(APIView):
    permission_classes=(IsAuthenticated,)
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
