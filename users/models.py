from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone
from django.db import models


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = None
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
