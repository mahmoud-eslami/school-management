from django.db import models
import uuid
from django.contrib.auth.models import User
from django.conf import settings
from school.validators import *

#############################
#role
MODERATION = '1'
ASSISTANT = '2'
TEACHER = '3'
STUDENT = '4'
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
six = '6'
seven = '7'
eight = '8'
nine = '9'
employee = '10'
#############################
#############################
#role choices
role_choices = [
    (MODERATION,'مدیر'),
    (ASSISTANT,'معاون'),
    (TEACHER,'معلم'),
    (STUDENT,'دانش آموز'),
]
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
    (six,'ششم'),
    (seven,'هفتم'),
    (eight,'هشتم'),
    (nine,'نهم'),
    (employee,'پرسنل'),
]
#############################


class userDoc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doc')
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    religion = models.CharField(max_length=100,blank=False,null=True)
    userPhoto = models.CharField(max_length=250,blank=True,null=True)
    userNationalCardPhoto = models.CharField(max_length=250,blank=True,null=True)
    userIdCardPhoto = models.CharField(max_length=250,blank=True,null=True)
    user_pNum = models.CharField(max_length=11,blank=False,null=True)
    home_pNum = models.CharField(max_length=11,blank=False,null=True)
    address = models.CharField(max_length=250,blank=False,null=True,)
    zipCode = models.CharField(max_length=10,blank=False,null=True)
    personalCode = models.CharField(max_length=10,blank=False,null=True,)
    nationalCode = models.CharField(max_length=10,blank=False,null=True,unique=True) # for being unique
    father_nationalCode = models.CharField(max_length=10,blank=True,null=True)
    father_name = models.CharField(max_length=40,blank=True,null=True)
    father_pNum = models.CharField(max_length=11,blank=True,null=True)
    father_jobName = models.CharField(max_length=50,blank=True,null=True)
    father_jobAddress = models.CharField(max_length=250,null=True,blank=True)
    father_job_pNum = models.CharField(max_length=11,blank=True,null=True)
    father_job_postalCode = models.CharField(max_length=10,blank=True,null=True)
    mother_nationalCode = models.CharField(max_length=10,blank=True,null=True)
    mother_name = models.CharField(max_length=40,blank=True,null=True)
    mother_pNum = models.CharField(max_length=11,blank=True,null=True)
    mother_jobName = models.CharField(max_length=50,blank=True,null=True)
    mother_jobAddress = models.CharField(max_length=250,null=True,blank=True)
    mother_job_pNum = models.CharField(max_length=11,blank=True,null=True)
    mother_job_postalCode = models.CharField(max_length=10,blank=True,null=True)
    citizen_Num = models.CharField(max_length=11,blank=True,null=True)
    date_of_birth = models.CharField(max_length=50,blank=False,null=True)
    place_of_birth = models.CharField(max_length=50,blank=False,null=True)
    role = models.CharField(max_length=1,choices=role_choices,default=STUDENT)
    citizen = models.CharField(max_length=1,default=IRAN,choices=citizen_choices)
    gender = models.CharField(max_length=1,choices=gender_choices,default=MAN)
    section = models.CharField(max_length=2,choices=section_choices,default=employee)
#========================================
#dashtane hamzaman  ta field
    class Meta:
        unique_together = ('user','nationalCode',)

class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads',blank=False,null=True,validators=[validate_image_size,])
