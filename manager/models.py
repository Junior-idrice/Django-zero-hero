from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.FileField(default='on.jpg', upload_to='profile_pictures')
    status_info = models.CharField(default="enter status", max_length=1000)

    def __str__(self):
        return f"{self.user.username} Profile"
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=2000)
    post_picture = models.FileField(default='on.jpg', upload_to='post_pictures')

    def __str__(self):
        return self.user.username
    
class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    following_user = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

class Follower(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    follower_user = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_text  = models.CharField(default="", max_length=1000)