'use strict';

const restify = require('restify'),
    controllers = require('./controllers');

class HttpServer {
    init() {
        this._restify = restify.createServer();

        this._initControllers();
    }

    listen(port) {
        this._restify.listen(port, () => console.log('Up & running'));
    }

    getRestify() {
        return this._restify;
    }

    _initControllers() {
        controllers.forEach(controller => controller.init(this._restify));
    }
}

module.exports = new HttpServer();
