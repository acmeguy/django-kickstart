var socketio = require("socket.io");
var redis = require("redis");

// redis clients
var sub = redis.createClient();

// ... application paths go here

var io = socketio.listen(8001);

sub.psubscribe("socketio_*");


io.sockets.on('connection', function(socket) {
	sub.on('pmessage', function(pattern,channel,key) {
		socket.emit(channel,key);
	});
})
