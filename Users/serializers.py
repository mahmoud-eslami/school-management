<<<<<<< HEAD
from rest_framework import serializers
from .models import *
from school.validators import *

class ModeratorChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)

class ChangePasswordInProfileSerilizer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    new_password = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)

class ImageSerilizer(serializers.Serializer):
    user_id = serializers.CharField(max_length=3,allow_blank=True,allow_null=False)
    image = serializers.ImageField(max_length=None, allow_empty_file=False,use_url=True,validators=[validate_image_size,])

    def create(self , validated_data):
        return Images.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    class Meta:
        model = MyUser
        exclude = ['password','last_login','is_superuser'
        ,'is_staff','is_active','groups','user_permissions']
        read_only_fields = ['username']

    def create(self , validated_data):
        return User.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.first_name = validated_data.get('first_name' , instance.first_name)
        instance.last_name = validated_data.get('last_name' , instance.last_name)
        instance.email = validated_data.get('email' , instance.email)
        instance.role = validated_data.get('role' , instance.role)
        instance.save()
        return instance

class UserDocSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(read_only=True)
    religion = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    userPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userNationalCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userIdCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    user_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=False)
    home_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=False)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=False)
    personalCode = serializers.CharField(max_length=10,allow_null=False,allow_blank=False)
    nationalCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=False)
    father_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    father_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    father_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    mother_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    mother_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    citizen_Num = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    date_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=False)
    place_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=False)
    citizen = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    gender = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    section = serializers.CharField(max_length=2,allow_blank=False,allow_null=False)

    def create(self , validated_data):
        return userDoc.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.religion = validated_data.get('religion' , instance.religion)
        instance.userPhoto = validated_data.get('userPhoto' , instance.userPhoto)
        instance.userNationalCardPhoto = validated_data.get('userNationalCardPhoto' , instance.userNationalCardPhoto)
        instance.userIdCardPhoto = validated_data.get('userIdCardPhoto' , instance.userIdCardPhoto)
        instance.user_pNum = validated_data.get('user_pNum' , instance.user_pNum)
        instance.home_pNum = validated_data.get('home_pNum' , instance.home_pNum)
        instance.address = validated_data.get('address' , instance.address)
        instance.zipCode = validated_data.get('zipCode' , instance.zipCode)
        instance.personalCode = validated_data.get('personalCode' , instance.personalCode)
        instance.nationalCode = validated_data.get('nationalCode' , instance.nationalCode)
        instance.father_nationalCode = validated_data.get('father_nationalCode' , instance.father_nationalCode)
        instance.father_name = validated_data.get('father_name' , instance.father_name)
        instance.father_pNum = validated_data.get('father_pNum' , instance.father_pNum)
        instance.father_jobName = validated_data.get('father_jobName' , instance.father_jobName)
        instance.father_jobAddress = validated_data.get('father_jobAddress' , instance.father_jobAddress)
        instance.father_job_pNum = validated_data.get('father_job_pNum' , instance.father_job_pNum)
        instance.father_job_postalCode = validated_data.get('father_job_postalCode' , instance.father_job_postalCode)
        instance.mother_nationalCode = validated_data.get('mother_nationalCode' , instance.mother_nationalCode)
        instance.mother_name = validated_data.get('mother_name' , instance.mother_name)
        instance.mother_pNum = validated_data.get('mother_pNum' , instance.mother_pNum)
        instance.mother_jobName = validated_data.get('mother_jobName' , instance.mother_jobName)
        instance.mother_jobAddress = validated_data.get('mother_jobAddress' , instance.mother_jobAddress)
        instance.mother_job_pNum = validated_data.get('mother_job_pNum' , instance.mother_job_pNum)
        instance.mother_job_postalCode = validated_data.get('mother_job_postalCode' , instance.mother_job_postalCode)
        instance.mother_jobAddress = validated_data.get('mother_jobAddress' , instance.mother_jobAddress)
        instance.citizen_Num = validated_data.get('citizen_Num' , instance.citizen_Num)
        instance.date_of_birth = validated_data.get('date_of_birth' , instance.date_of_birth)
        instance.place_of_birth = validated_data.get('place_of_birth' , instance.place_of_birth)
        instance.citizen = validated_data.get('citizen' , instance.citizen)
        instance.gender = validated_data.get('gender' , instance.gender)
        instance.section = validated_data.get('section' , instance.section)
        instance.save()
        return instance

# serialize data for register a new user
class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    last_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    email = serializers.EmailField(allow_null=False,allow_blank=True,max_length=100)
    role = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    religion = serializers.CharField(max_length=100,allow_blank=False,allow_null=True)
    userPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userNationalCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userIdCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    user_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=True)
    home_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=True)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=True)
    personalCode = serializers.CharField(max_length=10,allow_null=True,allow_blank=False)
    nationalCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=True)
    father_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    father_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    father_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    mother_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    mother_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    citizen_Num = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    date_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=True)
    place_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=True)
    citizen = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    gender = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    section = serializers.CharField(max_length=2,allow_blank=False,allow_null=True)
=======
from rest_framework import serializers
from .models import *
from school.validators import *

class ChangePasswordInProfileSerilizer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    new_password = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)

class ImageSerilizer(serializers.Serializer):
    user_id = serializers.CharField(max_length=3,allow_blank=False,allow_null=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False,use_url=True,validators=[validate_image_size,])

    def create(self , validated_data):
        return Images.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    class Meta:
        model = MyUser
        exclude = ['password','last_login','is_superuser'
        ,'is_staff','is_active','groups','user_permissions']
        read_only_fields = ['username']

    def create(self , validated_data):
        return User.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.first_name = validated_data.get('first_name' , instance.first_name)
        instance.last_name = validated_data.get('last_name' , instance.last_name)
        instance.email = validated_data.get('email' , instance.email)
        instance.role = validated_data.get('role' , instance.role)
        instance.save()
        return instance

class UserDocSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(read_only=True)
    religion = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    userPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userNationalCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userIdCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    user_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=False)
    home_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=False)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=False)
    personalCode = serializers.CharField(max_length=10,allow_null=False,allow_blank=False)
    nationalCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=False)
    father_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    father_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    father_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    mother_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    mother_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    citizen_Num = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    date_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=False)
    place_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=False)
    citizen = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    gender = serializers.CharField(max_length=1,allow_blank=False,allow_null=False)
    section = serializers.CharField(max_length=2,allow_blank=False,allow_null=False)

    def create(self , validated_data):
        return userDoc.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.religion = validated_data.get('religion' , instance.religion)
        instance.userPhoto = validated_data.get('userPhoto' , instance.userPhoto)
        instance.userNationalCardPhoto = validated_data.get('userNationalCardPhoto' , instance.userNationalCardPhoto)
        instance.userIdCardPhoto = validated_data.get('userIdCardPhoto' , instance.userIdCardPhoto)
        instance.user_pNum = validated_data.get('user_pNum' , instance.user_pNum)
        instance.home_pNum = validated_data.get('home_pNum' , instance.home_pNum)
        instance.address = validated_data.get('address' , instance.address)
        instance.zipCode = validated_data.get('zipCode' , instance.zipCode)
        instance.personalCode = validated_data.get('personalCode' , instance.personalCode)
        instance.nationalCode = validated_data.get('nationalCode' , instance.nationalCode)
        instance.father_nationalCode = validated_data.get('father_nationalCode' , instance.father_nationalCode)
        instance.father_name = validated_data.get('father_name' , instance.father_name)
        instance.father_pNum = validated_data.get('father_pNum' , instance.father_pNum)
        instance.father_jobName = validated_data.get('father_jobName' , instance.father_jobName)
        instance.father_jobAddress = validated_data.get('father_jobAddress' , instance.father_jobAddress)
        instance.father_job_pNum = validated_data.get('father_job_pNum' , instance.father_job_pNum)
        instance.father_job_postalCode = validated_data.get('father_job_postalCode' , instance.father_job_postalCode)
        instance.mother_nationalCode = validated_data.get('mother_nationalCode' , instance.mother_nationalCode)
        instance.mother_name = validated_data.get('mother_name' , instance.mother_name)
        instance.mother_pNum = validated_data.get('mother_pNum' , instance.mother_pNum)
        instance.mother_jobName = validated_data.get('mother_jobName' , instance.mother_jobName)
        instance.mother_jobAddress = validated_data.get('mother_jobAddress' , instance.mother_jobAddress)
        instance.mother_job_pNum = validated_data.get('mother_job_pNum' , instance.mother_job_pNum)
        instance.mother_job_postalCode = validated_data.get('mother_job_postalCode' , instance.mother_job_postalCode)
        instance.mother_jobAddress = validated_data.get('mother_jobAddress' , instance.mother_jobAddress)
        instance.citizen_Num = validated_data.get('citizen_Num' , instance.citizen_Num)
        instance.date_of_birth = validated_data.get('date_of_birth' , instance.date_of_birth)
        instance.place_of_birth = validated_data.get('place_of_birth' , instance.place_of_birth)
        instance.citizen = validated_data.get('citizen' , instance.citizen)
        instance.gender = validated_data.get('gender' , instance.gender)
        instance.section = validated_data.get('section' , instance.section)
        instance.save()
        return instance

# serialize data for register a new user
class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    last_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    email = serializers.EmailField(allow_null=False,allow_blank=True,max_length=100)
    role = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    religion = serializers.CharField(max_length=100,allow_blank=False,allow_null=True)
    userPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userNationalCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userIdCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    user_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=True)
    home_pNum = serializers.CharField(max_length=11,allow_blank=False,allow_null=True)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=True)
    personalCode = serializers.CharField(max_length=10,allow_null=True,allow_blank=False)
    nationalCode = serializers.CharField(max_length=10,allow_blank=False,allow_null=True)
    father_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    father_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    father_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    father_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    mother_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_jobName = serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)
    mother_job_pNum = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    mother_job_postalCode = serializers.CharField(max_length=10,allow_blank=True,allow_null=True)
    citizen_Num = serializers.CharField(max_length=11,allow_blank=True,allow_null=True)
    date_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=True)
    place_of_birth = serializers.CharField(max_length=50,allow_blank=False,allow_null=True)
    citizen = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    gender = serializers.CharField(max_length=1,allow_blank=False,allow_null=True)
    section = serializers.CharField(max_length=2,allow_blank=False,allow_null=True)
>>>>>>> dd13af56e1140249d9736fa2532530f84604ca64
