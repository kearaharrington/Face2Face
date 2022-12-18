from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from main_app.models import Chatroom, Message, Participant
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time


# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# ...and add the following line...
from django.contrib.auth.decorators import login_required
# Add LoginForm to this line...
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        print("Logged in")
    else:
        print("Not logged in")
    return render(request, 'index.html')

def create_chatroom(request):
    return render(request, 'createChatroom.html')

def lobby(request):
    return render(request, 'group/lobby.html')

def room(request):
    return render(request, 'group/room.html')

def getToken(request):
    #Build token with uid
    appId = '2743b5d3f8bd4737a2dff589a32dcaaa'
    appCertificate = '6b864506c34e492993b91224191dfd4b'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 200)
    expirationTimeInSeconds = 3600 * 200
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    
    
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    user_id = request.user.id
    chatrooms = Chatroom.objects.filter(creator=user)
    member_exists = Participant.objects.filter(user_id=user_id)
    if member_exists:
        member = Participant.objects.get(user_id=user_id)
        memberships = member.chatroom_set.all()
        return render(request, 'profile.html', {'username': username, 'chatrooms': chatrooms, 'memberships': memberships})
    else:
        return render(request, 'profile.html', {'username': username, 'chatrooms': chatrooms})

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
          return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def chatroom(request, chatroom):
    user = request.user
    chatroom = Chatroom.objects.get(name=chatroom)
    return render(request, 'main_app/message_form.html', {
        'user': user,
        'chatroom': chatroom,
    })
@login_required
def CreateChatroom(request):
    if request.method == 'POST': 
        chatroom = request.POST['chatroom']
        creator = request.user
        print('THIS IS CHATROOM!!', chatroom)
        if Chatroom.objects.filter(name=chatroom).exists():
            return redirect(f'/message/{chatroom}/create')
        else:
            new_room = Chatroom.objects.create(name=chatroom, creator=creator)
            new_room.save()
            return redirect(f'/message/{chatroom}/create')
    else: 
        all_chatrooms = Chatroom.objects.all()
        return render(request, 'createChatroom.html', {'all_chatrooms': all_chatrooms})

@login_required
def edit_chatroom(request, chatroom):
    chatroom = Chatroom.objects.get(name=chatroom)
    user = request.user
    # chatroom_name = str(chatroom.name)
    # print(chatroom_name)
    if user == chatroom.creator and request.method == 'GET':
        return render(request, "edit_chatroom.html", {'chatroom': chatroom})
    elif user == chatroom.creator and request.method == 'POST':
        name = request.POST['name']
        chatroom.name = name
        chatroom.save()
        return redirect(f'/message/{name}/create/')
    else: 
        return redirect(f'/message/{chatroom.name}/create')

@login_required
def delete_chatroom(request, chatroom):
    chatroom = Chatroom.objects.get(name=chatroom)
    user = request.user
    if user == chatroom.creator:
        chatroom.delete()
        return redirect('profile', username=user.username)
    else:
        return redirect('profile', username=user.username)

@login_required
def CreateMessage(request, chatroom):
    user = request.user
    chatroom = list(Chatroom.objects.filter(name=chatroom))[0]
    if request.method == 'POST': 
        text = request.POST['text']
        new_message = Message.objects.create(sender=user, chatroom=chatroom, text=text)
        new_message.save()
        participant_exists = Participant.objects.filter(user_id=user.id)
        if participant_exists:
            return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})
        elif new_message.sender != chatroom.creator and new_message.sender != chatroom.members:
            new_member = Participant.objects.create(user=user)
            new_member.save()
            chatroom.members.add(new_member)
            return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})
    else: 
        return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})


@login_required
def getMessages(request, chatroom):
    
    room_details = Chatroom.objects.get(name=chatroom)
    messages = Message.objects.filter(chatroom=room_details.id)
    # users = User.objects.get()
    # print('this is users!!!!', users)
    return JsonResponse({"messages":list(messages.values())})

