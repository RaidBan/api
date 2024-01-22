import json
from flask import jsonify


def rjsonin():
    with open("record.json", "r", encoding="windows-1251") as raw:
        data = json.load(raw)
    return data


def rjsonout(out):
    with open("record.json", "w", encoding="windows-1251") as done:
        #jsonify(out)
        json.dump(out, done, ensure_ascii=False, indent=4)


def sjsonin():
    with open("shift.json", "r", encoding="windows-1251") as raw:
        data = json.load(raw)
    return data

def sjsonout(out):
    with open("shift.json", "w", encoding="windows-1251") as done:
        json.dump(out, done, ensure_ascii=False, indent=4)