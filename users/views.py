from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from rest_framework import generics

User = get_user_model()

class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ListUsersApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer