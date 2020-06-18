# Generated by Django 3.0.6 on 2020-05-24 13:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import school.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('1', 'مدیر'), ('2', 'معاون'), ('3', 'معلم'), ('4', 'دانش آموز')], default='1', max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='uploads', validators=[school.validators.validate_image_size])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userDoc',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('religion', models.CharField(max_length=100, null=True)),
                ('userPhoto', models.CharField(blank=True, max_length=250, null=True)),
                ('userNationalCardPhoto', models.CharField(blank=True, max_length=250, null=True)),
                ('userIdCardPhoto', models.CharField(blank=True, max_length=250, null=True)),
                ('user_pNum', models.CharField(max_length=11, null=True)),
                ('home_pNum', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('zipCode', models.CharField(max_length=10, null=True)),
                ('personalCode', models.CharField(max_length=10, null=True)),
                ('nationalCode', models.CharField(max_length=10, null=True, unique=True)),
                ('father_nationalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('father_name', models.CharField(blank=True, max_length=40, null=True)),
                ('father_pNum', models.CharField(blank=True, max_length=11, null=True)),
                ('father_jobName', models.CharField(blank=True, max_length=50, null=True)),
                ('father_jobAddress', models.CharField(blank=True, max_length=250, null=True)),
                ('father_job_pNum', models.CharField(blank=True, max_length=11, null=True)),
                ('father_job_postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('mother_nationalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=40, null=True)),
                ('mother_pNum', models.CharField(blank=True, max_length=11, null=True)),
                ('mother_jobName', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_jobAddress', models.CharField(blank=True, max_length=250, null=True)),
                ('mother_job_pNum', models.CharField(blank=True, max_length=11, null=True)),
                ('mother_job_postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('citizen_Num', models.CharField(blank=True, max_length=11, null=True)),
                ('date_of_birth', models.CharField(max_length=50, null=True)),
                ('place_of_birth', models.CharField(max_length=50, null=True)),
                ('citizen', models.CharField(choices=[('1', 'اتباع ایرانی'), ('0', 'اتباع خارجی')], default='1', max_length=1)),
                ('gender', models.CharField(choices=[('1', 'آقا'), ('0', 'خانوم')], default='1', max_length=1)),
                ('section', models.CharField(choices=[('0', 'پیش دبستانی'), ('1', 'اول ابتدایی'), ('2', 'دوم ابتدایی'), ('3', 'سوم ابتدایی'), ('4', 'چهارم ابتدایی'), ('5', 'پنجم ابتدایی'), ('6', 'ششم'), ('7', 'هفتم'), ('8', 'هشتم'), ('9', 'نهم'), ('10', 'پرسنل')], default='10', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'nationalCode')},
            },
        ),
    ]
