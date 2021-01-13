from rest_framework import serializers
from .models import *
from school.validators import *


class ModeratorChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=100, allow_blank=False, allow_null=False)


class ChangePasswordInProfileSerilizer(serializers.Serializer):
    old_password = serializers.CharField(
        max_length=100, allow_blank=False, allow_null=False)
    new_password = serializers.CharField(
        max_length=100, allow_blank=False, allow_null=False)


class ImageSerilizer(serializers.Serializer):
    user_id = serializers.CharField(
        max_length=3, allow_blank=True, allow_null=False)
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, use_url=True, validators=[validate_image_size, ])

    def create(self, validated_data):
        return Images.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(
        max_length=1, allow_blank=False, allow_null=False)

    class Meta:
        model = MyUser
        exclude = ['password', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'groups', 'user_permissions']
        read_only_fields = ['username']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance


class UserDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDoc
        fields = '__all__'

    def create(self, validated_data):
        return userDoc.objects.create(**validated_data)