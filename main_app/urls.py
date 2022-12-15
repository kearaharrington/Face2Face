from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/create/', views.CreateChatroom, name='create_chatroom'),
    # path('chatroom/<str:chatroom>/', views.chatroom, name='chatroom'),
    path('message/<str:chatroom>/create/', views.CreateMessage, name='create_message'),
    path('getMessages/<str:chatroom>/', views.getMessages, name='getMessages'),
    
    # path('lobby/', views.lobby),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('group/', views.chatroom, name='chat_room'),
        path('', views.index, name='index'),
    path('room/', views.room),
    path('lobby/', views.lobby),
]

