'use strict';

const io = require('socket.io');

class SocketServer {
    init(restify) {
        this._io = io.listen(restify.server);

        this._io.on('connection', () => console.log('new client connected'));
    }

    send(messageName, message) {
        this._io.emit(messageName, message);
    }
}

module.exports = new SocketServer();
