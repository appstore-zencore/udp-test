udp-test
========

A simple udp server and client for network testing.


Install
-------

::

    pip install udp-test


Usage
-----

::

    E:\code\udp-test>udp-test --help
    Usage: udp-test [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    client
    server

    E:\code\udp-test>udp-test server --help
    Usage: udp-test server [OPTIONS]

    Options:
    -p, --port INTEGER
    --help              Show this message and exit.

    E:\code\udp-test>udp-test client --help
    Usage: udp-test client [OPTIONS]

    Options:
    -h, --host TEXT
    -p, --port INTEGER
    -l, --local-port INTEGER
    --help                    Show this message and exit.


Example
-------

::

    E:\code\udp-test>udp-test server
    Get a message from 127.0.0.1 : 55032 ==> hello

Simple command 'udp-test server' will start a udp server which listening port 5005 on all interfaces. The simple udp server will print the received message and send it back to the sender.

::

    E:\code\udp-test>udp-test client

Simple command 'udp-test client' will start a udp client that connect to the default server 127.0.0.1:5005. It will send every line message to the server and print the received message.

::

    E:\code\udp-test>udp-test server -p 1234

This command wills start a server listen port 1234 on all interfaces.

::

    E:\code\udp-test>udp-test client -h 123.123.123.123 -p 1234

This command will start a client that will send message to server 123.123.123.123:1234 via a random local port.

::

    E:\code\udp-test>udp-test client -h 123.123.123.123 -p 1234 -l 5678

This command will start a client that will send message to server 123.123.123.123:1234 via the given local port 5678.

