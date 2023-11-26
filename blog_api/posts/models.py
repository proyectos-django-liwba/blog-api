#importar model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    views = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    