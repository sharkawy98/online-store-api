from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer


User = get_user_model()


# users app API views (i.e controllers)
class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ListUsersApiView(generics.ListAPIView):
    permission_classes = (IsAdminUser,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer