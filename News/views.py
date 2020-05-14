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


class addNews(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
             serilized_data = serializers.addNewsSerializer(data=request.data)
             if serilized_data.is_valid():
                 news_title = serilized_data.data.get('title')
                 news_content = serilized_data.data.get('content')
                 news_author_id = serilized_data.data.get('author_id')
                 news_pic = request.FILES['pic']
                 news_release_data = datetime.now()
                 news_author = User.objects.get(id = news_author_id)
             else:
                 message = serilized_data.errors
                 return Response({"status_code":"400" , "error":"message","data":"","message":""},)
             #make instance from news
             new_news = News()
             new_news.title = news_title
             new_news.content = news_content
             new_news.release_date = news_release_data
             new_news.pic = news_pic
             new_news.author = news_author
             new_news.save()
             return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Added Success"},status.HTTP_200_OK)
        except Exception as e:
             trace_back = traceback.format_exc()
             message = str(e) + ' ' + str(trace_back)
             return Response({"status_code":"500" , "error": message,"data":"","message":""},)


class deleteNews(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            news_id = request.data['news_id']
            News.objects.all().filter(id = news_id).delete()
            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Deleted Success"},status.HTTP_200_OK)
        except:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error":message,"data":"","message":""},)


class editNews(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            serializer = serializers.editNewsSerializer(data=request.data)
            if serializer.is_valid():
                news_id = serializer.data.get('id')
                news_title = serializer.data.get('title')
                news_content = serializer.data.get('content')
                news_release_data = datetime.now()
                news_pic = request.FILES['pic']
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error":message,"data":"","message":""},)
            # update object in db
            if News.objects.all().filter(id = news_id).exists():
                temp_news = News.objects.get(id = news_id)
                temp_news.title = news_title
                temp_news.content = news_content
                temp_news.pic = news_pic
                temp_news.release_date = news_release_data
                temp_news.save()
            else:
                return Response({"status_code":"500" , "error": "object isn,t exists","data":"","message":""},)
            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Updated"},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)


class allNews(APIView):
    #permission_classes=(IsAuthenticated,)
    def get(self, request):
        try:
            temp_news = News.objects.all()
            serilized_data = serializers.allNewsSerializer(temp_news, many=True)
            json_data = serilized_data.data
            return Response({"status_code":"200" , "error":"", "data": json_data , "message":"" },status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)
