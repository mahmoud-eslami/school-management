from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *

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
