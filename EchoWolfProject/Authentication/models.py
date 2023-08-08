from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    profile_image = models.ImageField(upload_to='static/images/', default='static/images/user.png')
    