import sys
import socket
import click


def show_info(message, remote, prefix):
    if not sys.version.startswith("2"):
        message = message.decode("utf-8")
    info = "{prefix} {remote_ip} : {remote_port} ==> {message}".format(
        prefix=prefix,
        remote_ip=remote[0],
        remote_port=remote[1],
        message=message,
        )
    click.echo(info)


@click.group()
def test():
    pass


@test.command()
@click.option("-p", "--port", type=int, default=5005)
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    while True:
        message, remote = sock.recvfrom(1024*64)
        show_info(message, remote, "Get a message from")
        sock.sendto(message, remote)


@test.command()
@click.option("-h", "--host", default="127.0.0.1")
@click.option("-p", "--port", type=int, default=5005)
@click.option("-l", "--local-port", type=int, default=0)
def client(host, port, local_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if local_port:
        sock.bind(('0.0.0.0', local_port))
    while True:
        line = input("Send message: ")
        sock.sendto(line.encode("utf-8"), (host, port))
        message, remote = sock.recvfrom(1024*64)
        show_info(message, remote, "Received reply from")



if __name__ == "__main__":
    test()
