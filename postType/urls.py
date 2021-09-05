from django.contrib import admin
from django.urls import path
from .views import GenericAPIViewList

urlpatterns = [
    path('generic/postType/',GenericAPIViewList.as_view()),
    # path('generic/postType/<int:id>/',GenericAPIView.as_view()),
]