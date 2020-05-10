from django.db import models
import uuid
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nationalCode = models.CharField(max_length=10,blank=False,null=False,default='xxxxxxxxxx')

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
