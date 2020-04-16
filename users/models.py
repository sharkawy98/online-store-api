from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPES = (
        ('normal', 'Normal user'),
        ('owner', 'Store owner'),
        ('admin', 'Admin user'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.username
