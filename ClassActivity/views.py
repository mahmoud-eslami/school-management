from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from school.methods import CustomResponse
from .models import *
from rest_framework import status
from . import serializers


class PersentAbsentApi(APIView):
    permission_classes = (IsAuthenticated,)

    # get by date
    def get(self, request):
        try:
            day = request.GET['day']
            month = request.GET['month']
            year = request.GET['year']
            if PresentAbsentList.objects.filter(day=day, month=month, year=year).exists():
                temp_list = PresentAbsentList.objects.filter(
                    day=day, month=month, year=year)
                serializer = serializers.PresentAbsentSerializer(
                    temp_list, many=True)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=['دانش آموزی امروز مدرسه نیومده .'], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = serializers.PresentAbsentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message="دانش آموز با موفقیت به لیست اضاف شد .", data="", status=status.HTTP_200_OK)
            else:
                message = serializer.errors
                return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            user_id = request.GET['user_id']
            day = request.GET['day']
            month = request.GET['month']
            year = request.GET['year']
            if PresentAbsentList.objects.filter(day=day, month=month, year=year, user_id=user_id).exists():
                temp_row = PresentAbsentList.objects.get(
                    day=day, month=month, year=year, user_id=user_id)
                serializer = serializers.PresentAbsentSerializer(
                    temp_row, request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors=[], message="اطلاعات با موفقیت اپدیت شد .", data="", status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return CustomResponse(self, status_code=406, errors=['دانش آموزش مورد نظر امروز مدرسه نیومده .'], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            user_id = request.GET['user_id']
            day = request.GET['day']
            month = request.GET['month']
            year = request.GET['year']
            if PresentAbsentList.objects.filter(day=day, month=month, year=year, user_id=user_id).exists():
                temp_list = PresentAbsentList.objects.get(
                    day=day, month=month, year=year, user_id=user_id).delete()
                return CustomResponse(self, status_code=200, errors=[], message="دانش آموز مورد نظر از لیست حضور حذف شد .", data="", status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=['دانش آموزش مورد نظر امروز مدرسه نیومده .'], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllLessons(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            temp_all_lessons = Lessons.objects.all()
            serializer = serializers.LessonsSerializers(
                temp_all_lessons, many=True)
            return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class lessonsApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            lesson_id = request.GET['lesson_id']
            if Lessons.objects.all().filter(id=lesson_id).exists():
                temp_lesson = Lessons.objects.get(id=lesson_id)
                serializer = serializers.LessonsSerializers(temp_lesson)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="درس مورد نظر موجود نیست .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                serializer = serializers.LessonsSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors=[], message="درس با موفقیت ایجاد شد .", data="", status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                lesson_id = request.GET['lesson_id']
                if Lessons.objects.all().filter(id=lesson_id).exists():
                    Lessons.objects.get(id=lesson_id).delete()
                    return CustomResponse(self, status_code=200, errors=[], message="درس با موفقیت حذف شد .", data="", status=status.HTTP_200_OK)
                else:
                    return CustomResponse(self, status_code=406, errors=["درس با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                lesson_id = request.GET['lesson_id']
                if Lessons.objects.all().filter(id=lesson_id).exists():
                    temp_lesson = Lessons.objects.get(id=lesson_id)
                    serializer = serializers.LessonsSerializers(
                        temp_lesson, request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return CustomResponse(self, status_code=200, errors=[], message="درس با موفقیت ویرایش شد .", data="", status=status.HTTP_200_OK)
                    else:
                        message = serializer.errors
                        return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return CustomResponse(self, status_code=406, errors=["درس با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getClassWeeklySchedule(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            class_id = request.GET['class_id']
            if WeeklySchedule.objects.filter(class_id=class_id).exists():
                temp_schedule = WeeklySchedule.objects.filter(
                    class_id=class_id)
                serializer = serializers.WeeklyScheduleSerializer(
                    temp_schedule, many=True)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="برنامه ای برای کلاس مورد نظر تعریف نشده .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getLessonsBySection(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            section_id = request.GET['section_id']
            if Lessons.objects.filter(section_id=section_id).exists():
                temp_lessons = Lessons.objects.filter(section_id=section_id)
                serializer = serializers.LessonsSerializers(
                    temp_lessons, many=True)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="درسی برای مقطع مورد نظر وجود ندارد .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class weeklyScheduleApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            class_id = request.GET['class_id']
            week_day = request.GET['week_day']
            if WeeklySchedule.objects.filter(class_id=class_id, week_day=week_day).exists():
                temp_week = WeeklySchedule.objects.get(
                    class_id=class_id, week_day=week_day)
                serializer = serializers.WeeklyScheduleSerializer(temp_week)
                return CustomResponse(self, status_code=200, errors=[], message="", data=serializer.data, status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406, errors=[], message="برنامه مورد نظر یافت نشد .", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                serializer = serializers.WeeklyScheduleSerializer(
                    data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors=[], message="برنامه با موفقیت ایجاد شد .", data="", status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                class_id = request.GET['class_id']
                week_day = request.GET['week_day']
                if WeeklySchedule.objects.filter(week_day=week_day, class_id=class_id).exists():
                    temp_week = WeeklySchedule.objects.get(
                        week_day=week_day, class_id=class_id)
                    serializer = serializers.WeeklyScheduleSerializer(
                        temp_week, request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return CustomResponse(self, status_code=200, errors=[], message="برنامه با موفقیت ویرایش شد .", data="", status=status.HTTP_200_OK)
                    else:
                        message = serializer.errors
                        return CustomResponse(self, status_code=406, errors=message, message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return CustomResponse(self, status_code=406, errors=["برنامه با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            role = request.user.role
            if role == 3 or role == 4:
                return CustomResponse(self, status_code=403, errors=["شما دسترسی به این بخش را ندارید"], message="", data="", status=status.HTTP_403_FORBIDDEN)
            else:
                week_day = request.GET['week_day']
                class_id = request.GET['class_id']
                if WeeklySchedule.objects.filter(week_day=week_day, class_id=class_id).exists():
                    WeeklySchedule.objects.get(
                        week_day=week_day, class_id=class_id).delete()
                    return CustomResponse(self, status_code=200, errors=[], message="برنامه با موفقیت حذف شد .", data="", status=status.HTTP_200_OK)
                else:
                    return CustomResponse(self, status_code=406, errors=["برنامه با این ایدی وجود ندارد"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            patrace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
