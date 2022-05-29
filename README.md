# Video Content Miner Server
A server for getting youtube video transcript.

# How to Run
## Start
```
git clone https://github.com/twuoy/video-content-miner-server.git
cd video-content-miner-server
make up
```

## Stop
```
cd video-content-miner-server
make down

# if you also want to clean docker image of this server
make rm-img
```

# APIs
## - /transcript
```
endpoint: /api/transcript
method: post
args:
| Name |  Type  |   Description  |
|------|--------|----------------|
| url  | string | The video url. |
```
