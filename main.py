from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

courses = {
        1:{"name": "Python", "videos": 15},
        2:{"name": "Java", "videos": 6}
        }
class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses[course_id]

    def delete(self, course_id):
        del courses[course_id]
        return courses

    def post(self, course_id):
        par = reqparse.RequestParser()
        par.add_argument("name")
        par.add_argument("videos")
        courses[course_id] = par.parse_args()
        return courses


api.add_resource(Main, "/api/main/<int:course_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
