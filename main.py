from flask import Flask, Response
from flask_restful import Api, Resource, request, reqparse
import json

app = Flask(__name__)
api = Api()


def jsonin():
    with open("bd.json", "r") as raw:
        courses = json.load(raw)
    return courses


def jsonout(out):
    with open("bd.json", "w") as done:
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
        if course_id in course.keys():
            #return "This element is already exist"
            return Response("This element is already exist", status=400, mimetype='application/json')
        else:
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
        #try:
        #    par = reqparse.RequestParser()
        #    par.add_argument("name", type=str)
        #    par.add_argument("videos", type=str)
        #    req = par.parse_args()
        #    course[course_id] = req
        #    jsonout(course)
        #    return req
        #except:
        #    req = request.args
        #    course[course_id] = req
        #    jsonout(course)
        #    return req


    def put(self, course_id):
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

    #def options(self, course_id):
    #    resp = Response("Foo bar baz")
    #    resp.headers['Access-Control-Allow-Origin'] = '*'
    #    return resp


class Pass(Resource):
    def get(self):
        return course

    def post(self):
        return Response("Try add number of element", status=400, mimetype='application/json')

    def delete(self):
        return Response("Try add number of element", status=400, mimetype='application/json')

    def put(self):
        return Response("Try add number of element", status=400, mimetype='application/json')

api.add_resource(Main, "/api/main/<course_id>")
api.add_resource(Pass, "/api/main/")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
