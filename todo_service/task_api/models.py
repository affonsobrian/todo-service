from django.db import models

from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
