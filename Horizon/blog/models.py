from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=130, default='')
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
