from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)