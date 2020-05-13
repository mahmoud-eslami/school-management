from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class userDoc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doc')
    userPhoto = models.ImageField(upload_to='uploads',blank=True,null=True)
    nationalCardPhoto = models.ImageField(upload_to='uploads',blank=True,null=True)
    user_pNum = models.CharField(max_length=40,blank=False,null=True)
    home_pNum = models.CharField(max_length=40,blank=False,null=True)
    address = models.CharField(max_length=250,null=True,blank=False)
    zipCode = models.CharField(max_length=20,blank=False,null=True)
    personalCode = models.CharField(max_length=20,null=True,blank=True)
    nationalCode = models.CharField(max_length=20,blank=False,null=True)
    father_nationalCode = models.CharField(max_length=20,blank=False,null=True)
    father_name = models.CharField(max_length=40,blank=False,null=True)
    father_pNum = models.CharField(max_length=40,blank=False,null=True)
    father_jobAddress = models.CharField(max_length=250,null=True,blank=False)
    father_job_pNum = models.CharField(max_length=40,blank=False,null=True)
    mother_nationalCode = models.CharField(max_length=20,blank=False,null=True)
    mother_name = models.CharField(max_length=40,blank=False,null=True)
    mother_pNum = models.CharField(max_length=40,blank=False,null=True)
    mother_jobAddress = models.CharField(max_length=250,null=True,blank=False)
    mother_job_pNum = models.CharField(max_length=40,blank=False,null=True)
    citizen_Num = models.CharField(max_length=40,blank=True,null=True)
    date_of_birth = models.DateTimeField(blank=False,null=True)
    place_of_birth = models.CharField(max_length=40,blank=False,null=True)
    #############################
    #citizens
    IRAN = '1'
    NO_IRAN = '0'
    #gender
    MAN = '1'
    WOMAN = '0'
    #section
    pre_one = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    #############################
    #############################
    #citizens choices
    citizen_choices = [
        (IRAN,'اتباع ایرانی'),
        (NO_IRAN,'اتباع خارجی'),
    ]
    #gender choices
    gender_choices = [
        (MAN, 'آقا'),
        (WOMAN, 'خانوم'),
    ]
    # section choices
    section_choices = [
        (pre_one,'پیش دبستانی'),
        (one,'اول ابتدایی'),
        (two,'دوم ابتدایی'),
        (three,'سوم ابتدایی'),
        (four,'چهارم ابتدایی'),
        (five,'پنجم ابتدایی'),
    ]
    #############################

    citizen = models.CharField(max_length=1,default=IRAN,choices=citizen_choices)
    gender = models.CharField(max_length=1,choices=gender_choices,default=MAN)
    section = models.CharField(max_length=1,choices=section_choices,default=pre_one)




class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    #############################
    #role
    MODERATION = '1'
    ASSISTANT = '2'
    TEACHER = '3'
    STUDENT = '4'
    #role choices
    role_choices = [
        (MODERATION,'مدیر'),
        (ASSISTANT,'معاون'),
        (TEACHER,'معلم'),
        (STUDENT,'دانش آموز'),
    ]
    #############################

    role = models.CharField(max_length=1,choices=role_choices,default=STUDENT)

    #Magic Methods
    def __str__(self):
        return self.user.username
