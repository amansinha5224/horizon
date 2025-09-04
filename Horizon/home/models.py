from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100, default='')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Message form {self.name} | {self.email}"
