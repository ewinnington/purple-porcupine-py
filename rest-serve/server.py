from flask import Flask, request, json
import datetime
import uuid

events = [{"id" : str(uuid.uuid4()), "name" : "First Event", "created" : datetime.datetime.now() }]

api = Flask(__name__)

@api.route('/events', methods=['GET'])
def get_events():
    return json.dumps(events)

@api.route('/events', methods=['POST'])
def post_events():
    content = request.json
    e = {"id" : uuid.uuid4(), "name" : content['name'], "created" : datetime.datetime.now() }
    events.append(e)
    return json.dumps(e), 201

@api.route('/events/<string:id>', methods=['DELETE'])
def del_events(id):
    print(id)
    e = next((x for x in events if x["id"] == id), None)
    print(e)
    if (e != None):
        events.remove(e)
    return "", 204

@api.route('/', methods=['GET'])
def get_home():
    return 'Hello World'

if __name__ == '__main__': 
    api.run()