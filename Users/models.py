from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class userDoc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doc')
    address = models.CharField(max_length=250,null=False,blank=False)
    personalCode = models.IntegerField(null=True,blank=True)
    nationalCode = models.IntegerField(blank=False,null=True)
    father_nationalCode = models.IntegerField(blank=False,null=True)
    userPhoto = models.ImageField(upload_to='uploads',blank=True,null=True)
    nationalCardPhoto = models.ImageField(upload_to='uploads',blank=True,null=True)
    father_name = models.CharField(max_length=40,blank=False,null=True)
    mother_name = models.CharField(max_length=40,blank=False,null=True)
    father_pNum = models.CharField(max_length=40,blank=False,null=True)
    citizen_Num = models.CharField(max_length=40,blank=True,null=True)
    zipCode = models.IntegerField(blank=False,null=True)
    #############################
    #citizens
    IRAN = '1'
    NO_IRAN = '0'
    #############################
    #############################
    #citizens choices
    citizen_choices = [
        (IRAN,'اتباع ایرانی'),
        (NO_IRAN,'اتباع خارجی'),
    ]
    #############################
    citizen = models.CharField(max_length=40,default=IRAN,choices=citizen_choices)




class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    #############################
    #gender
    MAN = '1'
    WOMAN = '0'
    #role
    MODERATION = '1'
    ASSISTANT = '2'
    TEACHER = '3'
    STUDENT = '4'
    #############################
    #############################
    #gender choices
    gender_choices = [
        (MAN, 'آقا'),
        (WOMAN, 'خانوم'),
    ]
    #role choices
    role_choices = [
        (MODERATION,'مدیر'),
        (ASSISTANT,'معاون'),
        (TEACHER,'معلم'),
        (STUDENT,'دانش آموز'),
    ]
    #############################

    gender = models.CharField(max_length=4,choices=gender_choices,default=MAN)
    role = models.CharField(max_length=4,choices=role_choices,default=STUDENT)

    #Magic Methods
    def __str__(self):
        return self.user.username
