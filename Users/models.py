from django.db import models
from django.contrib.auth.models import  User
import uuid
class UserProfile(models.Model):


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key = True, editable = False , default = uuid.uuid4)

    def __str__(self):
        return self.user.username +' uuid ==> '+ str(self.uuid)

