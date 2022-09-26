from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
