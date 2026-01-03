from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique = True, max_length=50)
    photo_user = models.ImageField(upload_to="avatars/", blank=True,null=True)

    def __str__(self):
        return self.username