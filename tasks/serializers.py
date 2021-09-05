from django.db import models
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        #fields = ['id','title','details','date','post_type']
        fields = '__all__' 

class TaskSerializerList(serializers.ModelSerializer):
    post_type= serializers.StringRelatedField( read_only=True)
    class Meta:
        model= Task
        #fields = ['id','title','details','date','post_type']
        fields = '__all__' 