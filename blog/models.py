from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   
    
class User(AbstractUser):
    mobileNumber = models.IntegerField(null=True,blank=True)
    cityname = models.CharField(max_length=100,null=True,blank=True)
    statename = models.CharField(max_length=100,null=True,blank=True)
    # counteryname = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="name",blank=True, null=True)
    def __str__(self):
        return self.name