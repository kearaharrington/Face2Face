from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    topic = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(Participant, blank=True)
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
class Video_Chat(models.Model):
    participants = models.ManyToManyField(Participant)
    date = models.DateTimeField(auto_now_add=True)
    


# class Chatroom(models.Model):
#     name = models.CharField(max_length=1000)

# class Message(models.Model):
#     value = models.CharField(max_length=1000000)
#     date = models.DateTimeField(default=datetime.now, blank=True)
#     user = models.CharField(max_length=1000000)
#     chatroom = models.CharField(max_length=1000000)