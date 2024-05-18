from typing import Any
from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100,unique=True,null=False)
    password = models.CharField(max_length=100,null=False)
    username = models.CharField(max_length=100,null=False)
 

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    post_id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    subtitle = models.CharField(max_length=250,null=False)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=500,null=False)

    def __str__(self) -> str:
        return self.title 
