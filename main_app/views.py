from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from main_app.models import Group, Message

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

def chatroom(request, chatroom):
    username = request.GET.get('username')
    room_details = Group.objects.get(topic=chatroom)
    return render(request, 'chatroom.html', {
        'username': username,
        'chatroom': chatroom,
        'room_details': room_details
    })

@login_required
def checkview(request):
    chatroom = request.POST['group_topic']
    creator = request.user

    if Group.objects.filter(topic=chatroom).exists():
        return redirect('/'+chatroom+'/?creator='+creator.username)
    else:
        new_room = Group.objects.create(topic=chatroom, creator=creator)
        new_room.save()
        return redirect('/'+chatroom +'/?creator='+creator.username)

class send(CreateView):
  model = Message
  fields = '__all__'
  success_url = '/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.sender = self.request.user
    self.object.save()
    return HttpResponseRedirect('/')

def getMessages(request, chatroom):
    room_details = Group.objects.get(topic=chatroom)

    messages = Message.objects.filter(group=chatroom)
    return JsonResponse({"messages":list(messages.values())})