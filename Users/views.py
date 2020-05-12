from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *


class deleteUser(APIView):

    def post(self, request):
        try:
            pass
        except:
            pass


class getAllUser(APIView):

    def get(self, request):
        try:
            temp_users = User.objects.all()

            json_data = []

            for item in temp_users:

                temp_profile = userProfile.objects.get(user_id = item.id)
                temp_doc = userDoc.objects.get(user_id = item.id)

                # TODO: add serializer for image Field

                json_data.append({
                    'id':item.id,
                    'username':item.username,
                    'name':item.first_name,
                    'lname':item.last_name,
                    'email':item.email,
                    'date_joined':item.date_joined,
                    'userProfile':[
                        {'uuid':temp_profile.uuid,
                        'gender':temp_profile.gender,
                        'role':temp_profile.role,}
                    ],
                    'userDoc':[
                        {'address':temp_doc.address,
                        'zipCode':temp_doc.zipCode,
                        'citizen':temp_doc.citizen,
                        'citizen_Num':temp_doc.citizen_Num,
                        'personalCode':temp_doc.personalCode,
                        'nationalCode':temp_doc.nationalCode,
                        'nationalCardPhoto':str(temp_doc.nationalCardPhoto),
                        'date_of_birth':temp_doc.date_of_birth,
                        'place_of_birth':temp_doc.place_of_birth,
                        'father_name':temp_doc.father_name,
                        'father_nationalCode':temp_doc.father_nationalCode,
                        'father_pNum':temp_doc.father_pNum,
                        'mother_name':temp_doc.mother_name,
                        'userPhoto':str(temp_doc.userPhoto),}
                    ],
                })

            return Response({"status_code":"200" ,"error":"","data": json_data ,"message":""},status.HTTP_200_OK)
        except:
            return Response({'error' : 'Internal Server Error'})
