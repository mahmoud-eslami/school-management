from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from school.methods import CustomResponse
from .models import *
from rest_framework import status


class lessonsApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self , request):
        try:
            lesson_id = request.get['lesson_id']
            if Lessons.objects.all().filter(id = lesson_id).exist():
                return CustomResponse()
            else:
                return CustomResponse()
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)