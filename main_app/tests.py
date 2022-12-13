from django.test import TestCase

# Create your tests here.
# @method_decorator(login_required, name='dispatch')
# def send(request, self):
#     message = request.POST['message']
#     # username = request.POST['username']
#     room_id = request.POST['room_id']

#     sender = request.user
    
#     new_message = Message.objects.create(value=message, sender=sender, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')