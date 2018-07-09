from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length = 500)

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)