from django.urls import path

from .views import *

urlpatterns = [
    path('register', RegisterApiView.as_view(), name='register'),
    path('list', ListUsersApiView.as_view(), name='list'),
]