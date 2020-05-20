from django.db import models
from django.contrib.auth.models import User

class Classes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,blank=False,null=True)
