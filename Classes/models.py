from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# section
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
# section choices
section_choices = [
    (pre_one, 'پیش دبستانی'),
    (one, 'اول ابتدایی'),
    (two, 'دوم ابتدایی'),
    (three, 'سوم ابتدایی'),
    (four, 'چهارم ابتدایی'),
    (five, 'پنجم ابتدایی'),
    (six, 'ششم'),
    (seven, 'هفتم'),
    (eight, 'هشتم'),
    (nine, 'نهم'),
    (employee, 'پرسنل'),
]
#############################


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    section_id = models.CharField(
        max_length=2, choices=section_choices, default=pre_one, blank=False, null=False)

    def __str__(self):
        return str(self.id)


class UserClass(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_id', 'class_id']
