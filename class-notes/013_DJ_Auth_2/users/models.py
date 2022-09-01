from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)