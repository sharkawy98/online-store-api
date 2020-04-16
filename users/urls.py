from django.urls import path

from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', RegisterApiView.as_view(), name='register'),
    path('list', ListUsersApiView.as_view(), name='list'),
    path('login', obtain_auth_token, name='login')
]