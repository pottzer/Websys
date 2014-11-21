from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	username = models.CharField(max_length=254, unique=True)
	telephone = models.CharField(max_length=11, default=0)
	firstname = models.CharField(max_length=30, default=0)
	lastname = models.CharField(max_length=50, default=0)
	ssn = models.CharField(max_length=10, default=0)
	email = models.CharField(max_length=30, default=0)
	admin = models.BooleanField(default=False)
	USERNAME_FIELD = 'username'
