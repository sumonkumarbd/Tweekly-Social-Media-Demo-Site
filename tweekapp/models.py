from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Tweek(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField()  # Fixed: changed TextField to CharField
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255,default='Anonymous')
    user_photo = models.ImageField(
        upload_to='profile_photos/',
        default='defaults/default_user.png',
        blank=True,
        null=True
    )

