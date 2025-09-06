from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.comment[0:10]}... by {self.user.username}"