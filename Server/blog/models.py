from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.PROTECT)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Profile(models.Model):
    avatar = models.ImageField(default='profile_images/default.jpg', upload_to='profile_images')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username