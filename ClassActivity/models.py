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
day_one = '0'
day_two = '1'
day_three = '2'
day_four = '3'
day_five = '4'
day_six = '5'
day_seven = '6'
#############################
# section choices
week_day_choices = [
    (day_one, 'شنبه'),
    (day_two, 'یک شنبه'),
    (day_three, 'دو شنبه'),
    (day_four, 'سه شنبه'),
    (day_five, 'چهار شنبه'),
    (day_six, 'پنج شنبه'),
    (day_seven, 'جمعه'),
]
#############################
# grade type
mid = '1'
final = '2'
quiz = '0'
grade_type_choices = [(quiz, 'امتحان کلاسی'),
                       (mid, 'میانترم'), (final, 'پایان ترم'), ]
#############################
# grade content
very_low = '0'
low = '1'
medium = '2'
high = '3'
grade_count_choices = [
    (very_low, 'نیاز به تلاش بیشتر'),
    (low, 'قابل قبول'),
    (medium, 'خوب'),
    (high, 'خیلی خوب'),
]
#############################


class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    section_id = models.CharField(
        max_length=2, choices=section_choices, default=pre_one, blank=False, null=False)

    def __str__(self):
        return self.title


class WeeklySchedule(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(
        Classes, on_delete=models.CASCADE, blank=False, null=False)
    week_day = models.CharField(
        max_length=1, choices=week_day_choices, default=day_one, blank=False, null=False)
    first_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='first_bell', blank=False, null=False)
    second_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='second_bell', blank=False, null=False)
    third_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='third_bell', blank=False, null=False)
    forth_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='forth_bell', blank=False, null=False)
    fifth_bell = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name='fifth_bell', blank=False, null=False)

    class Meta:
        unique_together = ('class_id', 'week_day')


class AttendanceList(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day = models.CharField(max_length=5, blank=False, null=False)
    month = models.CharField(max_length=5, blank=False, null=False)
    year = models.CharField(max_length=5, blank=False, null=False)

    class Meta:
        unique_together = ('user_id','day','month','year')


class GradeList(models.Model):
    id = models.AutoField(primary_key=True)
    grade_owner_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='grade_owner')
    teacher_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='teacher')
    lesson_id = models.ForeignKey(Lessons,on_delete=models.CASCADE)
    grade_type = models.CharField(max_length=2,choices=grade_type_choices,null=False,blank=False)
    grade_count = models.CharField(max_length=2,choices=grade_count_choices,null=False,blank=False)
    day = models.CharField(max_length=5, blank=False, null=False)
    month = models.CharField(max_length=5, blank=False, null=False)
    year = models.CharField(max_length=5, blank=False, null=False)

    class Meta:
        unique_together = ('grade_owner_id','day','month','year','lesson_id')