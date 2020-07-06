from django.db import models

#section
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
    (pre_one,'پیش دبستانی'),
    (one,'اول ابتدایی'),
    (two,'دوم ابتدایی'),
    (three,'سوم ابتدایی'),
    (four,'چهارم ابتدایی'),
    (five,'پنجم ابتدایی'),
    (six,'ششم'),
    (seven,'هفتم'),
    (eight,'هشتم'),
    (nine,'نهم'),
    (employee,'پرسنل'),
]
#############################
class Lessons(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=250,blank=False,null=False)
    section_id = models.CharField(max_length=2,choices=section_choices,default=pre_one)