from django.contrib import admin

from .models import Participant, Chatroom, Message, Video_Chat

# Register your models here.
admin.site.register(Participant)
admin.site.register(Chatroom)
admin.site.register(Message)
admin.site.register(Video_Chat)

