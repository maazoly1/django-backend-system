from django.db import models
from django.contrib.auth.models import AbstractUser
from .enum import UserStatus
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    phone_no = models.CharField(max_length=14, unique=True, default='',)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=140, default='')
    profile_image = models.ImageField(upload_to="profile", default='',)
    status = models.CharField(
        max_length=16,
        choices=UserStatus.choices,
        default=UserStatus.UNVERIFIED,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()