from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,blank=False,null=True,unique=True)
    content = models.CharField(max_length=200,blank=False,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    pic = models.ImageField(upload_to='uploads',blank=True,null=True)
    release_date = models.DateTimeField()

    class Meta:
        unique_together = ('id','title',)
        
