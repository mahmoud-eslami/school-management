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
            username = request.data['username']
            email = request.data['email']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            password = request.data['password']

            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.save()

            return Response({"status_code":"200" ,"error":"","data": "" ,"message":"User Created"},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" ,"error":"Internal Server Error","data": "" ,"message":""},)

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
    permission_classes=(IsAuthenticated,)
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
