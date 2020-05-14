from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from Users.models import *
from datetime import datetime
from . import serializers

class addNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
             title = request.data['title']
             content = request.data['content']
             authorId = request.data['authorId']
             release_date = datetime.now()
             news_pic = request.FILES['news_pic']
             author = User.objects.get(id = authorId)
             #make instance from news
             new_news = News()
             new_news.title = title
             new_news.content = content
             new_news.release_date = release_date
             new_news.news_pic = news_pic
             new_news.author = author
             new_news.save()
             return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Added Success"},status.HTTP_200_OK)
        except Exception as e:
             return Response({"status_code":"500" , "error": str(e),"data":"","message":""},)


class deleteNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            news_id = request.data['news_id']

            News.objects.all().filter(id = news_id).delete()

            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Deleted Success"},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" , "error":"Internal Server Error","data":"","message":""},)

class editNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            news_id = request.data['news_id']
            title = request.data['title']
            content = request.data['content']
            release_date = datetime.now()
            news_pic = request.FILES['news_pic']

            News.objects.all().filter(id = news_id).update(title = title,content = content,release_date = release_date,news_pic = news_pic)

            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Updated"},status.HTTP_200_OK)

        except:
            return Response({"status_code":"500" , "error":"Internal Server Error","data":"","message":""},)

class allNews(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        try:
            temp_news = News.objects.all()
            serilized_data = serializers.allNewsSerializer(temp_news, many=True)
            json_data = serilized_data.data
            return Response({"status_code":"200" , "error":"", "data": json_data , "message":"" },status.HTTP_200_OK)
        except Exception as e:
            return Response({"status_code":"500" , "error":str(e),"data":"","message":""},)
