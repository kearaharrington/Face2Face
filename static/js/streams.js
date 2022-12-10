const APP_ID = 'f2d8a61a099e45c196cda215293e0b74'
const CHANNEL = 'main'
const TOKEN = '007eJxTYODdxNSxz+KVRfiHh5Kn6i4duBNkVaBoWMNqKfGYR5BjS48CQ5pRikWimWGigaVlqolpsqGlWXJKopGhqZGlcapBkrnJtDdTkhsCGRku/FFjZWSAQBCfhSE3MTOPgQEA2qoeUg=='
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})
let localTracks = []
let remoteUser = {}

let joinAndDisplayLocalStream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                  <div><span class="username-wrapper">My Name</span></div>
                  <div class="video-player" id="user-${UID}"></div>
                  </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)
    await client.publish([localTracks[0], localTracks[1]])
}

joinAndDisplayLocalStream()