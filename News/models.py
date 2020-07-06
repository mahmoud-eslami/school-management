from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.conf import settings

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=False,null=True,unique=True)
    content = models.CharField(max_length=5000,blank=False,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')
    pic = models.CharField(max_length=250,blank=True,null=True)
    release_date = models.CharField(max_length=50,blank=False,null=True)

    class Meta:
        unique_together = ('id','title',)
