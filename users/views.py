from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer


User = get_user_model()


# custom Permission for the user_type --> 'admin'
class permissionsToViewList(IsAdminUser):
    def has_permission(self,request,view):
        return request.user.user_type == 'admin'


# users app API views (i.e controllers)

class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ListUsersApiView(generics.ListAPIView):
    permission_classes = (permissionsToViewList,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer