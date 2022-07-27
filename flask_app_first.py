from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("name", type= str, location="form", help= "Enter Name of the video")
parser.add_argument("views", type= int, location="form", help= "Enter Views of the video")
parser.add_argument("likes", type= int, location="form", help= "Enter Likes of the video")

videos = {}

class Index(Resource):
    def get(self):
        return "Welcome to my API"

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = parser.parse_args()
        return json.dumps({video_id: args})

api.add_resource(Index, "/")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=81, debug=True)
