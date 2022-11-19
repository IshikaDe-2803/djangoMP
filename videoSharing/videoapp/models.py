from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class NewVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title =  models.CharField(max_length=100, default="")
    description = TextField(max_length=100, default="")
    visits= models.IntegerField(default="0")
    likes = models.IntegerField(default="0")
    dislikes = models.IntegerField(default="0")
    date = models.CharField(default=" ", max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnail_uploaded', default=None)
    video = models.FileField(upload_to='videos_uploaded', validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    video = models.ForeignKey(NewVideo, on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.comment_text
