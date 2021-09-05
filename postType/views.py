from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .serializers import PostTypeSerializer
from .models import PostType

# Create your views here.
class GenericAPIViewList(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,):
    serializer_class = PostTypeSerializer
    queryset = PostType.objects.order_by('-create_date')

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)