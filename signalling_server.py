import socketio
import uvicorn
from starlette.applications import Starlette

ROOM = 'room'


sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
star_app = Starlette(debug=True)
app = socketio.ASGIApp(sio, star_app)


@sio.event
async def connect(sid, environ):
    await sio.emit('ready', room=ROOM, skip_sid=sid)
    sio.enter_room(sid, ROOM)


@sio.event
async def data(sid, data):
    await sio.emit('data', data, room=ROOM, skip_sid=sid)


@sio.event
async def disconnect(sid):
    sio.leave_room(sid, ROOM)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8003)
