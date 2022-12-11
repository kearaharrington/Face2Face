from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room),
    path('lobby/', views.lobby),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('group/', views.chat_room, name='chat_room'),
]

