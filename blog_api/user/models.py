from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.URLField(max_length=200, blank=True)
    cellphone = models.CharField(max_length=20, blank=True)
    
    # cambiar el campo username por email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# blank=True: permite que el campo sea opcional
# null=True: permite que el campo sea opcional en la bd
# max_length: longitud maxima del campo
# unique=True: campo unico
