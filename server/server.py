from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import config

'''
API 
Namespace:
time - recieves the time and make adjustment if needed

connect : is triggered when the client is successfully connected to the server
message : is triggered when the client sends data
join : is tiggered when the client 
disconnect : is triggered when the client loses the connection with the server, 
    -closing the browser, dropping the connection, etc.

'''

# Creating an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = config.Config.SECRET_KEY

socketio = SocketIO(app, logger=True, engineio_logger=True,
                    cors_allowed_origins='*')


socketio.room_users = {}
socketio.reqid_info = {}


print("[Server Started] : " + config.Config.ADRESS)

# Communication Functions To The Client


@socketio.on('connect')
def connect_handler():
    print('[Client Connected]')
    socketio.emit("Connected")


@socketio.on('disconnect')
def test_disconnect():
    print('[Client Disconnected]')

@socketio.on('join')
def handle_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    print(f"{username} Joined Chat {room}")


@socketio.on('event')
def handle_message(json):
    data = dict(json)
    if "time" in data:
        print(data["time"])

    socketio.emit('message response', json)


if __name__ == '__main__':
    socketio.run(app, debug=config.Config.DEBUG)