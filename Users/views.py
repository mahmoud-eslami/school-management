from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *


class getAllUser(APIView):

    def get(self, request):
        #try:
            temp_users = User.objects.all()
            temp_profile = userProfile.objects.all()
            temp_doc = userDoc.objects.all()
            json_data = []





            for item in temp_users:

                json_data.append({
                    'id':item.id,
                    'username':item.username,
                    'name':item.first_name,
                    'lname':item.last_name,
                    'email':item.email,
                })
            return Response({"status_code":"200" ,"error":"","data": json_data ,"message":""},status.HTTP_200_OK)
        #except:
            #return Response({'error' : 'Internal Server Error'})
