from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    
    def __str__(self):
        return f"{self.user.username}'s profile"

# Model Follow
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following') # Empêche les doublons
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.follower} -> {self.following.username}"

# Model Post
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username}'s post at {self.created_at}"
