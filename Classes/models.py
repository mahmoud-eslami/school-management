from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,blank=False,null=True,unique=True)

    def __str__(self):
        return str(self.id)

class UserClass(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    userClass = models.ForeignKey(Classes,on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user','userClass']
