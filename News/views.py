from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from school.methods import *
from .models import *
from Users.models import *
from datetime import datetime
from . import serializers
import traceback

class NewsApi(APIView):
    permission_classes = (IsAuthenticated,)
    ########################## get method for recieve seprate news
    def get(self , request):
        try:
            id = request.GET['id']
            if News.objects.all().filter(id = id).exists():
                news = News.objects.get(id = id)
            else:
                return CustomResponse(self, status_code=406, errors=["خبر با این ایدی موجود نیست"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.NewsSerializer(news)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
             trace_back = traceback.format_exc()
             message = str(e) + ' ' + str(trace_back)
             return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ########################## post method for recieve seprate news
    def post(self , request):
        try:
            serializer = serializers.NewsSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message="خبر با موفقیت ایجاد شد", data="", status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ########################## delete method for delete seprate news
    def delete(self , request):
        try:
            id = request.GET['id']
            if News.objects.all().filter(id = id).exists():
                news = News.objects.get(id = id)
            else:
                return CustomResponse(self, status_code=406, errors=["خبر با این ایدی موجود نیست"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            news.delete()
            return CustomResponse(self, status_code=200, errors="", message="خبر با موفقیت حذف شد", data=[], status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ########################## put method for update seprate news
    def put(self ,request):
        try:
            id = request.GET['id']
            if News.objects.all().filter(id = id).exists():
                news = News.objects.get(id = id)
            else:
                return CustomResponse(self, status_code=406, errors=["خبر با این ایدی موجود نیست"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = serializers.NewsSerializer(news,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors="", message="خبر با موفقیت اپدیت شد", data=[], status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
