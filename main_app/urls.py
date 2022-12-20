from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/create/', views.CreateChatroom, name='createChatroom'),
    path('<str:chatroom>/update/', views.edit_chatroom, name='edit_chatroom'),
    path('<str:chatroom>/delete/', views.delete_chatroom, name='delete_chatroom'),
    path('<str:chatroom>/<str:member>/delete/', views.delete_member, name='delete_member'),
    path('message/<str:chatroom>/create/', views.CreateMessage, name='create_message'),
    path('getMessages/<str:chatroom>/', views.getMessages, name='getMessages'),
    path('user/<username>/', views.profile, name='profile'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('group/', views.chatroom, name='chat_room'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('room/', views.room),
    path('lobby/', views.lobby),
    path('get_token/', views.getToken),
]

