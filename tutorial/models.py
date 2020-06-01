from django.db import models
from django.contrib.auth.models import User
from school.validators import *
from django.conf import settings

class Tutorial (models.Model):
    # in theis class you can upload pdf for tutorial
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=250,blank= False , null= False)
    content = models.CharField(max_length=250 ,blank= False , null = False)
    writer  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='writer')
    release_date = models.CharField(max_length=100,blank= False , null= True)
    tfile = models.CharField(max_length= 250 , blank= True, null = True)




class File(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads',blank=False,null=True,validators=[validate_file_size,validate_format_file ])
