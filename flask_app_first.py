from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("name", type= str, help= "Name of the video")
parser.add_argument("views", type= int, help= "Views of the video")
parser.add_argument("likes", type= int, help= "Likes of the video")

videos = {}

class Index(Resource):
    def get(self):
        return "Welcome to my API"

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = parser.parse_args()
        return {video_id: args}

api.add_resource(Index, "/")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)