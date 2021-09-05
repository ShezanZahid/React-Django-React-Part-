from django.db import models
from rest_framework import serializers
from .models import PostType

class PostTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= PostType
        #fields = ['id','title','author','post_type_name']
        fields = '__all__'