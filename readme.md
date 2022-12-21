# Face2Face
### Face2Face allows users to create and join virtual meeting rooms where they can communicate with each other using video, audio and instant messaging.


## Texting Chatroom 
### Users are able to create a chatroom and/or join an existing chatrooms.
#### New Chatroom - 
  ##### Simply type a chatroom name within the input and select "entering this room"
  ##### ![image](https://user-images.githubusercontent.com/107300143/208799407-89acbba6-8733-4c7e-a517-cf97eea662a6.png)
#### Existing Chatroom - 
  ##### Select the existing chatroom and it redirects to that page. 
  ##### ![image](https://user-images.githubusercontent.com/107300143/208799497-6df28c0f-31be-4191-9529-fd83588ccd09.png)
### Within the Chatroom 
#### Chatroom Header and Room name
  ##### ![image](https://user-images.githubusercontent.com/107300143/208799825-046a34e7-e786-4e11-a755-5235627d9d36.png)
#### Chat text 
 ##### 1. Username 2. Texting message 3. Date of the message created
 ##### ![image](https://user-images.githubusercontent.com/107300143/208800140-10073eec-6edf-40be-8f22-609d554bb618.png)
#### Sending the message
  ##### ![image](https://user-images.githubusercontent.com/107300143/208800279-ece2c086-edc8-461d-951f-dce7773bf5ed.png)

#### ![image](https://user-images.githubusercontent.com/107300143/208800342-e9d2167a-d069-4152-9bd9-23d14bec611d.png)

### Some notable codes
#### Fetching Messages "GET"
    <script>
      $(document).ready(function () {
        setInterval(function () {
          $.ajax({
            type: "GET",
            url: "/getMessages/{{chatroom}}/",
            success: function (response) {
              console.log(response);
              $("#display").empty();
              for (let key in response.messages) {
                let displayMessage =
                  "<div class='padding-box box container darker'><b>" +
                  response.messages[key].sender.toUpperCase() +
                  "</b><p class='container font'>" +
                   response.messages[key].text +
                  "</p><span class='padding-box darker'>" +
                  response.messages[key].created_at.slice(0, 10)+
                  "</span></div>";
                $("#display").append(displayMessage);
              }
            },
            error: function (response) {
              alert("Your message has not been sent, An Error");
            },
          });
        }, 1000);
      });
    </script>

