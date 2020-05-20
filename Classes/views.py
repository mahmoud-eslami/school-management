from django.shortcuts import render
from school.methods import *
from school.validators import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
import traceback

class GetAllClasses(APIView):
    permission_classes=(IsAuthenticated,)
    try:
        
    except Exception as e:

class ClassesApi(APIView):
    pass
