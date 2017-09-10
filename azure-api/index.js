'use strict';

const httpServer = require('./httpServer'),
    socketServer = require('./socketServer');

httpServer.init();
socketServer.init(httpServer.getRestify());

httpServer.listen(process.env.PORT || 8080);
