from django.contrib import admin
from django.urls import path
from .views import GenericAPIViewList,GenericAPIView,GenericAPIViewListList

urlpatterns = [
    path('generic/tasklist/',GenericAPIViewListList.as_view()),
    path('generic/task/',GenericAPIViewList.as_view()),
    path('generic/task/<int:id>/',GenericAPIView.as_view()),
]