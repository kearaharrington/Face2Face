from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:chatroom>/', views.chatroom, name='chatroom'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send.as_view(), name='send'),
    path('getMessages/<str:chatroom>/', views.getMessages, name='getMessages'),
    # path('lobby/', views.lobby),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]

