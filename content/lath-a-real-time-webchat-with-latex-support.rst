Lath. A real time webchat with LaTeX support.
#############################################
:date: 2013-10-22 20:13
:author: aesptux
:category: JavaScript, Programming, Project
:slug: lath-a-real-time-webchat-with-latex-support

Lath is a real-time minimalistic webchat with LaTeX support (I know the
name is not the best, it comes from LaTeX + Math). Rooms are predefined,
and right now there are three: Calculus, Discrete Mathematics and Logic,
because it is focused to CS students (based in Spain courses). Lath is
built with NodeJS and ExpressJS, MathJax for LaTeX and it stores each
message to a MySQL database. The code has three parts:

-  **index.html:** the html served with ExpressJS
-  **index.js:** Server side JS, a.k.a NodeJS
-  **client.js: **\ Client side JS.

You can find the complete source code on `Github`_. I'm going to comment
only some parts of the code: The most interesting part of the index.html
is the JavaScript:

::

    MathJax.Hub.Config({
            extensions: ["tex2jax.js","TeX/AMSmath.js","TeX/AMSsymbols.js"],
            jax: ["input/TeX", "output/HTML-CSS"],
            tex2jax: {
                inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                processEscapes: true
            },
            "HTML-CSS": { availableFonts: ["TeX"] }
        });

This is the configuration required for MathJax. It is interesting to
have the \ *processEscapes* *= true, *\ so you can escape LaTeX. Server
side:

::

    var express = require('express');
    var path = require('path');
    var mysql = require('mysql');
    var app = express();
    var port = 3700;
    var pool = mysql.createPool({
        host     : '',
        user     : '',
        password : '',
        database : 'lath'
    });

    // statics
    app.use(express.static(path.join(__dirname, 'public')));

    // define usernames
    var usernames = {};

    // define rooms
    var rooms = ['Calculus', 'Discrete Mathematics', 'Logic'];

    // routes
    app.get('/', function (req, res) {
        res.sendfile(__dirname + '/index.html');
    });

    // socket
    var io = require('socket.io').listen(app.listen(port));

    // define events
    io.sockets.on('connection', function (socket) {

        // when clients emit...

        socket.on('sendchat', function(data) {
            io.sockets.to(socket.room).emit('updatechat', socket.username, data);
            data = data.replace(/\\/g, '\\\\');
            pool.getConnection(function(err, connection) {
              // Use the connection
              connection.query('INSERT INTO chat_log(username, message, room) \
                VALUES ("' + socket.username + '", "' + data + '", "' +
                    socket.room + '")', function(err, rows) {
                // release connection, do not close
                connection.release();

              });
            });

        });

        socket.on('adduser', function(username) {
            socket.username = username;
            if (usernames[socket.username]) {
                socket.emit('connect', true);
                return 0;
            }
            socket.room = 'Calculus';
            usernames[username] = username;
            socket.join('Calculus');
            socket.emit('updatechat', 'SERVER', 'You have connected to Calculus.');
            // broadcast to all users
            socket.broadcast.to('Calculus').emit('updatechat', 'SERVER',
                username + ' has connected.');
            // update list client side
            io.sockets.emit('updateusers', usernames);
            socket.emit('updaterooms', rooms, 'Calculus');
        });

        socket.on('switchroom', function (newroom) {
            socket.leave(socket.room);
            socket.join(newroom);
            socket.emit('updatechat', 'SERVER', 'You have connected to ' +
                newroom + '.');
            socket.broadcast.to(socket.room).emit('updatechat', 'SERVER',
                socket.username + ' has left the room.');
            socket.room = newroom;
            socket.broadcast.to(socket.room).emit('updatechat', 'SERVER',
                socket.username + ' has joined the room');
            socket.emit('updaterooms', rooms, newroom);

        });

        // sad panda is sad with this event
        socket.on('disconnect', function() {
            delete usernames[socket.username];
            io.sockets.emit('updateusers', usernames);
            // broadcast
            socket.broadcast.emit('updatechat', 'SERVER',
                socket.username + ' has disconnected.');
            socket.leave(socket.room);
        });

    });

    console.log('Listening...');

This is the entire server-side part. I create a connection pool and not
a regular connection, because the regular one would be always active,
ending up in timeout due the keep alive. With the connection pool, the
connection is released after each query.

After defining some variables and routes (ExpressJS), we get to the
socket.io part. It reacts to certain events. For example, if it receives
a sendchat event, it stores the message on the DB. With sockets you can
also emit broadcast messages to all users, or to certain users (given a
room, for example).

::

    socket.broadcast.emit // will emit to all users

    socket.broadcast.to('myroom').emit // will emit to the users on that room (channel)

Client part:

::

    var socket = io.connect('http://localhost:3700');


    // get elements
    var users = document.getElementById('users');
    var rooms_list = document.getElementById('rooms');
    var conversation = document.getElementById('conversation');
    var txt = document.getElementById('data');
    var btnsend = document.getElementById('datasend');
    var content = document.getElementById('content');


    socket.on('connect', function (exists) {
        var username = null;
        console.log(exists);
        while (username == null) {
            if (exists) {
                username = prompt('The username is taken. Please, choose another.');
            } else {
                username = prompt('Set your username');
            }

        }
        socket.emit('adduser', username);
    });


    socket.on('updatechat', function (username, data) {
        conversation.innerHTML += '<b class="user">' + username +
            ': </b><span class="message">' + data + '</span><br />';
        // update MathJax with new DOM elements
        MathJax.Hub.Queue(["Typeset",MathJax.Hub,"conversation"]);
        content.scrollTop = content.scrollHeight;

    });


    socket.on('updaterooms', function (rooms, current_room) {
        console.log('Updating rooms');
        rooms_list.innerHTML = "";
        console.log(rooms);
        for (var room in rooms) {
            if (rooms[room] == current_room) {
                rooms_list.innerHTML += '<div><b>' + rooms[room] + '</b></div>';
            } else {
                rooms_list.innerHTML += '<div><a href="#" \
                onclick="switchRoom(\''+rooms[room]+'\')">' + rooms[room] +
                '</a></div>';
            }
        }
    });


    socket.on('updateusers', function (data) {
        users.innerHTML = "";
        for (var user in data) {
            users.innerHTML += "<div class='user'>" + data[user] + "</div>";
        }
    });


    function switchRoom(room) {
        console.log('Changing room');
        socket.emit('switchroom', room);
    }


    window.onload = function () {
        btnsend.addEventListener('click', function () {
            console.log('asfsd');
            socket.emit('sendchat', document.getElementById('data').value);
            document.getElementById('data').value = '';

        }, false);

        txt.addEventListener('keypress', function (e) {
            if (e.keyCode == 13) {
                btnsend.click();
            }

        }, false)

    }

 

It does not use jQuery as you can see, although it can ease the code
sometimes, for a project like this I think it is not necessary and it
will only be an overhead. This part starts with the connection to the
web socket and then getting the HTML elements we will be working with.
Then, I define some event listeners and emitters.  It is quite similar
to the server-side, only that here we can also work with the DOM
elements.

And that's all the code.

This is behind a nginx acting as a reverse proxy. The minimum version of
nginx for a project using web sockets is 1.3 (I have 1.4).

Once it is installed, it's pretty similar to other configurations:

::

    upstream app_server_lath {
        server localhost:3700 fail_timeout=0;
    }

    server {
            listen 80;
            server_name lath.aesptux.com www.lath.aesptux.com;

        keepalive_timeout 5;

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            # the following is required as well for WebSockets
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            if (!-f $request_filename) {
                proxy_pass http://app_server_lath;
                break;
            }
        }

       location /socket.io/ {
            proxy_pass http://localhost:3700;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
    }

    }

Thanks.

.. _Github: http://www.github.com/aesptux/lath
