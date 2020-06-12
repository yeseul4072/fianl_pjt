from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Profile(models.Model):
    image = ProcessedImageField(upload_to='',processors=[ResizeToFill(100,100)],blank=True, null=True)
    myinfo = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
