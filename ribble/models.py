from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    terms = models.CharField(max_length=10)
    avatar = models.FileField(upload_to="media/", max_length=250, null=True, default=None)
    location = models.TextField(max_length=250, null=True, default=None)

# class profile_det(models.Model):
#     avatar = models.FileField(upload_to="news/", max_length=250, null=True, default=None)
#     location = models.TextField(max_length=250, null=True, default=None)

