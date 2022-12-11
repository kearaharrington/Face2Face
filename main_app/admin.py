from django.contrib import admin

from .models import Participant, Group, Message, Video_Chat, Room

# Register your models here.
admin.site.register(Participant)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(Video_Chat)
admin.site.register(Room)
