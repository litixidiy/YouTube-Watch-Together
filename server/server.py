from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit,join_room, leave_room, \
close_room, rooms, disconnect

import config

#Creating an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = config.Config.SECRET_KEY

socketio = SocketIO(app,logger=True, engineio_logger=True,cors_allowed_origins='*')
print("[Server Started] : " +config.Config.ADRESS )

#Communication Functions To The Client
@socketio.on('connect')
def test_connect():
    print('[Client Connected]')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('event')
def handle_message(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server
    and sending message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """
    data = dict(json)
    '''if "time" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])'''

    socketio.emit('message response', json)


if __name__ == '__main__':
    socketio.run(app,debug=config.Config.DEBUG)