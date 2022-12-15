from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from main_app.models import Chatroom, Message

# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# ...and add the following line...
from django.contrib.auth.decorators import login_required
# Add LoginForm to this line...
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_chatroom(request):
    return render(request, 'createChatroom.html')

def lobby(request):
    return render(request, 'group/lobby.html')

def room(request):
    return render(request, 'group/room.html')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'username': username})

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
        return render(request, 'createChatroom.html')

@login_required
def CreateMessage(request, chatroom):
    if request.method == 'POST': 
        # user_id = int(request.POST['user_id'])
        # chatroom_id = int(request.POST['chatroom_id'])
        # print('user id here!', request.user, 'chatroom id here!', chatroom_id)
        text = request.POST['text']
        chatroom_name = request.POST['chatroom_name']

        chatroom = list(Chatroom.objects.filter(name=chatroom))[0]
        new_message = Message.objects.create(sender=request.user, chatroom=chatroom, text=text)
        print('THIS IS a new Message!!!', new_message.sender)
        new_message.save()
        return redirect(f'/getMessages/{chatroom_name}')
    else: 
        user = request.user
        print('printing CHATROOM 1', chatroom)
        chatroom = list(Chatroom.objects.filter(name=chatroom))[0]
        print('printing CHATROOM', chatroom)
        return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})



@login_required
def getMessages(request, chatroom):
    room_details = Chatroom.objects.get(name=chatroom)

    messages = Message.objects.filter(chatroom=room_details.id)
    return JsonResponse({"messages":list(messages.values())})