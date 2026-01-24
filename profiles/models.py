from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django import forms

class User(AbstractUser):
    email = models.EmailField(unique = True, max_length=50)
    photo_user = models.ImageField(upload_to="avatars/", blank=True,null=True)

    def __str__(self):
        return self.username
    
class Livre(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    titre = models.CharField(unique=False, max_length=100)
    couverture = models.ImageField(upload_to="couverture/",blank=True,null=True)
    description=models.CharField(max_length=1000)
    def __str__(self):
        return self.titre

class Chapitre(models.Model):
    livre = models.ForeignKey(
        Livre,
        on_delete=models.CASCADE,
        related_name="chapitres"
    )
    numero_chap = models.IntegerField()
    titre_chap = models.CharField(max_length=50)
    contenu= RichTextField()

class Meta:
    unique_together=('livre','numero_chap')