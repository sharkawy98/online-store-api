from django.shortcuts import render
from rest_framework.permissions import IsAdminUser

# Create your views here.
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from rest_framework import generics

User = get_user_model()

class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

class permissionsToViewList(IsAdminUser):
    def has_permission(self,request,view):
        return request.user.user_type == 'admin'

class ListUsersApiView(generics.ListAPIView):
    permission_classes = (permissionsToViewList,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer