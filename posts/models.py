from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='img', default='default.jpeg')
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
