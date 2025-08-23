import socket  # noqa: F401

TEXT_ENCODING = 'utf-8'
CRLF = '\r\n'
HTTP_VERSION = 'HTTP/1.1'

def send_request(messages: list[str], n_crlf = 2) -> bytes:
    message = HTTP_VERSION + ' ' + CRLF.join(messages) + (CRLF * n_crlf)
    return message.encode(TEXT_ENCODING)

def read_request(content: bytes) -> dict[str, str]:
    lines = content.decode(TEXT_ENCODING).split(CRLF)
    first_line = lines[0].split(' ')

    method, target, http_version = first_line[:3]
    headers = {}

    for line in lines[1:len(lines) - 2]:
        key, value = line.split(': ')
        headers[key] = value

    request = {
        'method': method,
        'target': target,
        'http_version': http_version,
        'headers': headers,
    }

    return request

def route(client: socket.socket, target: str) -> int:
    if target == '/':
        return client.send(send_request(['200 OK']))
    return client.send(send_request(['404 Not Found']))

def main():
    print("Server listing at localhost:4221")

    server_socket = socket.create_server(("localhost", 4221))
    client, address = server_socket.accept() # wait for client
    request_data = client.recv(1024)

    data = read_request(request_data)
    target = data['target']

    print(f'Connection accepted from {address}')
    route(client, target)

if __name__ == "__main__":
    main()
