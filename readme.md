# Face2Face (United States)

Face2Face is an online message board and video chatting app.


# Face2Face App

Visit Face2Face app website at: <a href=""> Face2Face</a>
<hr />

## Getting Started

`1` `Fork` & `Clone` this repo to your local computer.

`2` pip install packages
```text
pip3 install python-dotenv  
pip3 install psycopg2  
pip3 install agora_token_builder

```
<hr />

## Languages & Technologies

* `Django`
* `Postgres`
* Deployed to `Heroku`
* Agora video streaming

<hr />

## WireFrame
<img width="1239" alt="WireFrame" src="./static/imgs/Face2Face_Final.drawio.png">

<hr />

## User Stories

* Face2Face allows users to create and join virtual meeting rooms where they can communicate with each other using video, audio and instant messaging. Additional future improvements include features that can give participants the ability to share their screen, share files, and use text chat within the meeting group or privately with others in the meeting.

<hr />

## App Pictures

* Home Page
<img width="782" alt="home page" src="./static/imgs/homepage.png">

<br/>

* Login
<img width="969" alt="login" src="./static/imgs/login.png">

<br/>

* Create Chatroom
<img width="969" alt="create chatroom" src="./static/imgs/createchatroom.png">

<br/>

* Video Chat Lobby
<img width="797" alt="video chat lobby" src="./static/imgs/lobby.png">

<br/>

* Video Chat Stream
<img width="797" alt="video chat stream" src="./static/imgs/videochatstream.png">

<br/>

* Profile
<img width="797" alt="Profile" src="./static/imgs/profile.png">

<br/>



<hr />

## API's used

* Third party API: 
<br/>
<a href="https://www.agora.io/en/products/interactive-live-streaming/">Agora Video Streaming</a>
<br/>

### Models


### URL Paths
|url|view|
|'' | views.index|
|'chatroom/create/'| views.CreateChatroom|
|'<str:chatroom>/update/'| views.edit_chatroom|
|'<str:chatroom>/delete/'| views.delete_chatroom|
|'<str:chatroom>/<str:member>/delete/'| views.delete_member|
|'message/<str:chatroom>/create/'| views.CreateMessage|
|'getMessages/<str:chatroom>/'| views.getMessages|
|'user/<username>/'| views.profile|
|'accounts/login/'| views.login_view|
|'logout/'| views.logout_view|
|'signup/'| views.signup_view|
|'group/'| views.chatroom|
|'about/'| views.about|
|'contact/'| views.contact|
|'room/'| views.room|
|'lobby/'| views.lobby|
|'get_token/'| views.getToken|

### Code:
examples from main_app>views.py:
```python
@login_required
def CreateChatroom(request):
    if request.method == 'POST': 
        chatroom = request.POST['chatroom']
        creator = request.user
        if Chatroom.objects.filter(name=chatroom).exists():
            return redirect(f'/message/{chatroom}/create')
        else:
            new_room = Chatroom.objects.create(name=chatroom, creator=creator)
            new_room.save()
            return redirect(f'/message/{chatroom}/create')
    else: 
        all_chatrooms = Chatroom.objects.all()
        return render(request, 'createChatroom.html', {'chatrooms': all_chatrooms})

@login_required
def edit_chatroom(request, chatroom):
    chatroom = Chatroom.objects.get(name=chatroom)
    user = request.user
    members = list(chatroom.members.all())
    all_members = []
    for member in members:
        one_member = User.objects.get(id=member.user_id)
        all_members.append(one_member)
    if user == chatroom.creator and request.method == 'GET':
        return render(request, "edit_chatroom.html", {'chatroom': chatroom, 'members': all_members})
    elif user == chatroom.creator and request.method == 'POST':
        name = request.POST['name']
        chatroom.name = name
        chatroom.save()
        return redirect(f'/message/{name}/create/')
    else: 
        return redirect(f'/message/{chatroom.name}/create')

@login_required
def CreateMessage(request, chatroom):
    user = request.user
    chatroom = list(Chatroom.objects.filter(name=chatroom))[0]
    members = chatroom.members.all()
    # create new message
    if request.method == 'POST': 
        text = request.POST['text']
        new_message = Message.objects.create(sender=user, chatroom=chatroom, text=text)
        new_message.save()
        # check if user_id is already associated with participant instance
        participant_exists = Participant.objects.filter(user_id=user.id)
        # check to see if participant exists and needs to be added to chatroom instance
        if participant_exists and new_message.sender != chatroom.creator and participant_exists != members:
            new_member = Participant.objects.get(user_id=user.id)
            chatroom.members.add(new_member)
            chatroom.save()
            return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})
        # check to see if participant needs to be created and added to chatroom instance
        elif new_message.sender != chatroom.creator and new_message.sender != chatroom.members:
            new_member = Participant.objects.create(user=user)
            new_member.save()
            chatroom.members.add(new_member)
            chatroom.save()
            return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})
        else:
            return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})
    else: 
        return render(request, 'main_app/message_form.html', {'user': user, 'chatroom': chatroom})

```

## Developers 

<div>
    <h3> Aiden Jang </h3>
        <a href="https://github.com/AidenValley">Github</a>
    <h3> Keara Harrington </h3>
        <a href="https://github.com/kearaharrington">Github</a>
    <h3> Calvin Moldenhauer </h3>
        <a href="https://github.com/Calvickauer">Github</a>
    <h3> Alejandro Moreno </h3>
        <a href="https://github.com/amoreno16003">Github</a>
</div>

# Face2Face Future Improvements:
```
- [ ] make chatrooms private
- [ ] view all live video chats
- [ ] save video chat history to database

```