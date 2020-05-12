from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *


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
                # TODO: add serializer for image Field
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
