from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
