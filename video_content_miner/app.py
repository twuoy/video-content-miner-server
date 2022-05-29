from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from miner import YoutubeMiner

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "content-type"}})

@app.route('/api/health', methods=['GET'])
def health():
    message = 'Video content miner is running!'
    response = make_response(jsonify(message), 200)
    return response

@app.route('/api/transcript', methods=['POST'])
def get_transcript():
    youtube_url = request.get_json(force=True).get('url')
    print(f'Get transcript for {youtube_url=}')
    video_id = YoutubeMiner.get_video_id(youtube_url)
    transcript = YoutubeMiner.get_transcript(video_id)

    response = make_response(jsonify(transcript), 200)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
