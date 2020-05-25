from rest_framework import serializers
from .models import *

class TutorialSerilizer(serializers.ModelSerializer):
    class Meta :
        model = Tutrial
        fields = '__all__'
        read_only_fields = ['writer']

    def create(self , validated_data):
        return Tutrial.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.content = validated_data.get('content' , instance.content)
        instance.writer = validated_data.get('writer' , instance.writer)
        instance.ttype = validated_data.get('ttype' , instance.ttype)
        instance.tfile = validated_data.get('tfile' , instance.tfile)
        instance.save()
        return instance
