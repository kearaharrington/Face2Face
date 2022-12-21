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
```jsx

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
- [ ] Mark journeys as complete/expired after the date passes

```