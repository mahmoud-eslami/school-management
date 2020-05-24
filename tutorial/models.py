from django.db import models
from django.contrib.auth.models import User
from school.validators import *
from django.conf import Settings


pv = "0"
public = "1"
#==========


#====================================
#section choice for post massage for all user or specefic user
post_type_choice = [
(pv,"پست شخصی"),
(public, "عمومی"),
]

#===================================

class Tutrial (models.Model):
    # in theis class you can upload pdf for tutorial
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=250,blank= False , null= True)
    content = models.CharField(max_length=250 , blank= False , null = True)
    writer  = models.ForeignKey(Settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')
    ttype = models.CharField(choices= post_type_choice,max_length = 1, blank = False ,default= public)
    tfile = models.CharField(max_length= 250 , blank= True, null = True)




class file (models.Model):
    user = models.ForeignKey(Settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads',blank=False,null=True,validators=[validate_file_size , format_file ])
