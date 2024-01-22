from flask import Flask, Response
from flask_restful import Api, Resource, request, reqparse
from apijson import *
from datetime import date
import json

app = Flask(__name__)
api = Api()


datar = rjsonin()
datas = sjsonin()


class num(Resource):
    def get(self, bdname, data_id):
        if bdname == "record":
            if data_id == "0":
                return datar
            elif data_id in datar.keys():
                return datar[data_id]
            else:
                return Response("Данной записи не существует", status=400, mimetype='application/json')
        elif bdname == "shift":
            if data_id == "0":
                return datas
            elif data_id in datas.keys():
                return datas[data_id]
            else:
                return Response("Данной записи не существует", status=400, mimetype='application/json')
        else:
            return Response("Данной базы данных не существует", status=400, mimetype='application/json')

    def delete(self, bdname, data_id):
        del data[data_id]
        jsonout(data)
        return data

    def put(self,bdname, data_id):
        if bdname == "record":
            try:
                par = reqparse.RequestParser()
                par.add_argument("ФИО")
                par.add_argument("Почта")
                par.add_argument("Телефон")
                par.add_argument("Смена")
                req = par.parse_args()
                for i in req.keys():
                    a = i
                print("parser", req, a)
                datar[data_id][a] = req[a]
                rjsonout(datar)
                return req
            except:
                req = request.args.to_dict()
                for i in req.keys():
                    a = i
                datar[data_id][a] = req[a]
                rjsonout(datar)
                return req
        elif bdname == "shift":
            try:
                par = reqparse.RequestParser()
                par.add_argument("ДатаНачала")
                par.add_argument("ДатаОкончания")
                par.add_argument("КоличествоНомерков")
                req = par.parse_args()
                for i in req.keys():
                    a = i
                print(req[req.keys()])
                datas[data_id][a] = req[a]
                print(datas[data_id][req.keys])
                sjsonout(datas)
                return req
            except:
                req = request.args.to_dict()
                for i in req.keys():
                    a = i
                datas[data_id][a] = req[a]
                sjsonout(datas)
                return req
        else:
            return Response("Данной базы данных не существует", status=400, mimetype='application/json')
class nonum(Resource):
    def post(self, bdname):

        today = date.today()
        if bdname == "record":
            data_id = len(datar) + 1
            try:
                par = reqparse.RequestParser()
                par.add_argument("ФИО")
                par.add_argument("Почта")
                par.add_argument("Телефон")
                par.add_argument("Смена")
                req = par.parse_args()
                datar[data_id] = req
                datar["ДатаЗаписи"] = str(today)
                rjsonout(datar)
                return req
            except:
                req = request.args.to_dict()
                datar[data_id] = req
                datar[data_id]["ДатаЗаписи"] = str(today)
                rjsonout(datar)
                return req
        elif bdname == "shift":
            data_id = len(datas) + 1
            try:
                par = reqparse.RequestParser()
                par.add_argument("ДатаНачала")
                par.add_argument("ДатаОкончания")
                par.add_argument("КоличествоНомерков")
                req = par.parse_args()
                datas[data_id] = req
                sjsonout(datas)
                return req
            except:
                req = request.args.to_dict()
                datas[data_id] = req
                sjsonout(datas)
                return req
        else:
            return Response("Данной базы данных не существует", status=400, mimetype='application/json')


api.add_resource(num, "/api/<bdname>/<data_id>")
api.add_resource(nonum, "/api/<bdname>/")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.0.21")