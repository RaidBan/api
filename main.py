from flask import Flask, jsonify
from flask_restful import Api, Resource, request, reqparse
import json

app = Flask(__name__)
api = Api()


def jsonin():
    with open("courses.json", "r") as raw:
        courses = json.load(raw)
    return courses


def jsonout(out):
    with open("courses.json", "w") as done:
        json.dump(out, done, ensure_ascii=False, indent=4)


course = jsonin()


class Main(Resource):
    def get(self, course_id):
        if course_id == '0':
            return course
        else:
            return course[course_id]

    def delete(self, course_id):
        del course[course_id]
        jsonout(course)
        return course

    def post(self, course_id):
        try:
            par = reqparse.RequestParser()
            par.add_argument("name", type=str)
            par.add_argument("videos", type=str)
            req = par.parse_args()
            course[course_id] = req
            jsonout(course)
            return req
        except:
            req = request.args
            course[course_id] = req
            jsonout(course)
            return req


api.add_resource(Main, "/api/main/<course_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
