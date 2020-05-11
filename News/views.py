from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from Users.models import *
from datetime import datetime

class addNews(APIView):

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
        except:
             return Response({"status_code":"500" , "error":"Internal Server Error","data":"","message":""},)


class deleteNews(APIView):

    def post(self, request):
        try:
            news_id = request.data['news_id']

            News.objects.all().filter(id = news_id).delete()

            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Deleted Success"},status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" , "error":"Internal Server Error","data":"","message":""},)
"""
class editNews(APIView):

    def post(self, request):
        #try:
            news_id = request.data['news_id']


        #except:
            #pass
"""
class allNews(APIView):

    def get(self, request):
        try:
            temp_news = News.objects.all()

            json_data = []

            for item in temp_news:
                json_data.append({
                    'auther_id':item.author_id,
                    'auther_username':item.author.username,
                    'post_id':item.id,
                    'title':item.title,
                    'contact':item.content,
                    'release_date':item.release_date,
                })

            return Response({"status_code":"200" , "error":"", "data": json_data , "message":"" },status.HTTP_200_OK)
        except:
            return Response({"status_code":"500" , "error":"Internal Server Error","data":"","message":""},)
