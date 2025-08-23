import socket  # noqa: F401

import httplib


def listen(host: str, port: int) -> tuple[socket.socket, str]:
    server_socket = socket.create_server((host, port))
    return server_socket.accept() # wait for client

def parse_request(client: socket.socket):
    request_data = client.recv(1024)
    return httplib.read_request(request_data)

def route(client: socket.socket, target: str) -> int:
    if target == '/':
        return client.send(httplib.send_request(['200 OK']))
    return client.send(httplib.send_request(['404 Not Found']))
