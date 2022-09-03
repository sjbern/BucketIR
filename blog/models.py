from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    #these are the fields of a post, or attributes
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #deletes posts if user is deleted.

    def __str__(self):
        return self.title