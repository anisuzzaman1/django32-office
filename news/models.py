from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=220)
    content =  models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True, default=timezone.now)
    #updated = models.DateTimeField(auto_now=True)
    #publish =  models.DateField()