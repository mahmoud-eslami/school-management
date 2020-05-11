from django.db import models
from django.conf import settings

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,blank=False,null=True)
    content = models.CharField(max_length=20,blank=False,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')
    news_pic = models.ImageField(upload_to='uploads',blank=True,null=True)
    release_date = models.DateTimeField()

    
