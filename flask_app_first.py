from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("name", type= str, location="form", help= "Enter Name of the video")
parser.add_argument("views", type= int, location="form", help= "Enter Views of the video")
parser.add_argument("likes", type= int, location="form", help= "Enter Likes of the video")

videos = {}

def no_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Video does not exist.")

def al_exists(video_id):
    if video_id in videos:
        abort(409, message = "Video already exists.")

class Index(Resource):
    def get(self):
        return "Welcome to my API"

class Video(Resource):
    def get(self, video_id):
        no_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        al_exists(video_id)
        args = parser.parse_args()
        videos[video_id] = args
        return json.dumps(videos[video_id])

    def delete(self, video_id):
        no_exist(video_id)
        del videos[video_id]
        return {"message": "Deleted successfully"}

api.add_resource(Index, "/")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=81, debug=True)
