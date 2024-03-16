from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    document = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    plan = models.CharField(max_length=20, default='Free')
    
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []