from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import TaskSerializer, TaskSerializerList
from .models import Task

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class JWTAuthenticationSafe(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request=request)
        except InvalidToken:
            return None

# Create your views here.
class GenericAPIViewList(generics.GenericAPIView, mixins.CreateModelMixin,):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthenticationSafe]
    queryset = Task.objects.order_by('-created_date')

    def post(self,request):
        return self.create(request)

    

class GenericAPIViewListList(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = TaskSerializerList
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthenticationSafe]
    queryset = Task.objects.order_by('-created_date')

    def get(self,request):
        return self.list(request)

    
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
    mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthenticationSafe]
    queryset= Task.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id = None):
        return self.destroy(request,id)