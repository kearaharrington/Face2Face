from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

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