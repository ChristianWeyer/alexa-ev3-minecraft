'use strict';

const socketServer = require('../../socketServer');

class DoItDudeController {
    init(restify) {
        restify.get('/doitdude', this._doItDude.bind(this));
    }

    _doItDude(req, res) {
        socketServer.send('doItDude');
        res.send(200);
    }
}

module.exports = new DoItDudeController();
