from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

import datetime


@socketio.on('joined', namespace='/home')
def joined(data):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = data['room']
    join_room(room)
    emit('status', {'msg': data['user'] +
                    ' has switched/entered the [' + room + '] room.', 'room': room}, room=room)


@socketio.on('login', namespace='/home')
def login(message):
    room = 'public'
    join_room(room)
    emit('newUser', {
        'users': session.get('users'),
        'rooms': session.get('rooms'),
        'currentUser': session.get('users')[len(session.get('users')) - 1]
    }, room=room)


@socketio.on('text', namespace='/home')
def text(data):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = data['room']
    date = datetime.datetime.now().time().strftime("%H:%M:%S")
    emit('message', '[' + data['user'] + ']@[' +
         date + ']in[' + room + ']:  ' + data['msg'], room=room)


@socketio.on('left', namespace='/home')
def left(data):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = data['room']
    leave_room(room)
    emit('status', {'msg': data['user'] +
                    ' has left the [' + room + '] room.'})
