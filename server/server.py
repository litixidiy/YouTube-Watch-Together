from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

#Creating an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testplswork'
socketio = SocketIO(app,logger=True, engineio_logger=True,cors_allowed_origins='*')

@socketio.on('connect')
def test_connect(auth):
    print('[Client Connected]')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app)