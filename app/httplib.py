from dataclasses import dataclass

TEXT_ENCODING = 'utf-8'
CRLF = '\r\n'
HTTP_VERSION = 'HTTP/1.1'

@dataclass(frozen=True)
class Request:
    method: str
    target: str
    http_version: str
    headers: dict[str, str]


def send_request(messages: list[str], n_crlf = 2) -> bytes:
    message = HTTP_VERSION + ' ' + CRLF.join(messages) + (CRLF * n_crlf)
    return message.encode(TEXT_ENCODING)

def read_request(content: bytes) -> Request:
    lines = content.decode(TEXT_ENCODING).split(CRLF)
    first_line = lines[0].split(' ')

    method, target, http_version = first_line[:3]
    headers = {}

    for line in lines[1:len(lines) - 2]:
        key, value = line.split(': ')
        headers[key] = value

    return Request(method, target, http_version, headers)
