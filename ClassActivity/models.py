from django.db import models
from Classes.models import Classes
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
# weekDay
day_one = '1'
day_two = '2'
day_three = '3'
day_four = '4'
day_five = '5'
day_six = '6'
#############################
# section choices
week_day_choices = [
    (day_one, 'شنبه'),
    (day_two, 'یک شنبه'),
    (day_three, 'دو شنبه'),
    (day_four, 'سه شنبه'),
    (day_five, 'چهار شنبه'),
    (day_six, 'پنج شنبه'),
]
#############################


class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    section_id = models.CharField(
        max_length=2, choices=section_choices, default=pre_one,blank=False, null=False)

    def __str__(self):
        return self.title


class WeeklySchedule(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE,blank=False, null=False)
    week_day = models.CharField(
        max_length=1, choices=week_day_choices, default=day_one,blank=False, null=False)
    first_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='first_bell',blank=False, null=False)
    second_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='second_bell',blank=False, null=False)
    third_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='third_bell',blank=False, null=False)
    forth_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='forth_bell',blank=False, null=False)
    fifth_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='fifth_bell',blank=False, null=False)

    def __str__(self):
        return self.week_day + str(self.class_id)

    class Meta:
        unique_together = ('class_id', 'week_day')



class PresentAbsentList(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    day = models.CharField(max_length=5,blank=False,null=False)
    month = models.CharField(max_length=5,blank=False,null=False)
    year = models.CharField(max_length=5,blank=False,null=False)


        