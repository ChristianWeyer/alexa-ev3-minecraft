'use strict';

const socketServer = require('../../socketServer');

class MoveController {
    init(restify) {
        restify.get('/move/forward', this._forward.bind(this));
        restify.get('/move/backward', this._backward.bind(this));
        restify.get('/move/stop', this._stop.bind(this));
    }

    _forward(req, res) {
        socketServer.send('move', 'forward');
        res.send(200);
    }

    _backward(req, res) {
        socketServer.send('move', 'backward');
        res.send(200);
    }

    _stop(req, res) {
        socketServer.send('move', 'stop');
        res.send(200);
    }
}

module.exports = new MoveController();
