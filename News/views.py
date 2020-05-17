from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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
                return Response({"status_code":"400" , "error": ["خبر با این ایدی موجود نیست"],"data":"","message":""},)
            serializer = serializers.NewsSerializer(news)
            return Response({"status_code":"200" , "error":[], "data": serializer.data , "message":""},status.HTTP_200_OK)
        except Exception as e:
             trace_back = traceback.format_exc()
             message = str(e) + ' ' + str(trace_back)
             return Response({"status_code":"500" , "error": message,"data":"","message":""},)

    ########################## post method for recieve seprate news
    def post(self , request):
        try:
            serializer = serializers.NewsSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"status_code":"200" , "error": [],"data":"","message":"خبر با موفقیت ایجاد شد"},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": message ,"data":"","message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)

    ########################## delete method for delete seprate news
    def delete(self , request):
        try:
            id = request.GET['id']
            if News.objects.all().filter(id = id).exists():
                news = News.objects.get(id = id)
            else:
                return Response({"status_code":"400" , "error": ["خبر با این ایدی موجود نیست"],"data":"","message":""},)
            news.delete()
            return Response({"status_code":"200" , "error":"", "data": [] , "message":"خبر با موفقیت حذف شد"},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)

    ########################## put method for update seprate news
    def put(self ,request):
        try:
            id = request.GET['id']
            if News.objects.all().filter(id = id).exists():
                news = News.objects.get(id = id)
            else:
                return Response({"status_code":"400" , "error": ["خبر با این ایدی موجود نیست"],"data":"","message":""},)
            serializer = serializers.NewsSerializer(news,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code":"200" , "error": "","data":[],"message":"خبر با موفقیت اپدیت شد"},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error": message ,"data":"","message":""},)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)
