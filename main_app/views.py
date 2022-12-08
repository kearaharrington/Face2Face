from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')