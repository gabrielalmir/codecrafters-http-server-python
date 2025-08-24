from dataclasses import dataclass

from constants import CRLF, TEXT_ENCODING
from errors import InvalidRequest


@dataclass(frozen=True)
class Request:
    method: str
    target: str
    http_version: str
    headers: dict[str, str]

    @staticmethod
    def read_request(content: bytes):
        sections = content.decode(TEXT_ENCODING).split(CRLF+CRLF)
        lines = [line for section in sections for line in section.split(CRLF)]

        if not lines:
            raise InvalidRequest("No content to decode in request")

        first_line = lines[0].split(' ')

        method, target, http_version = first_line[:3]
        headers = {}

        for line in lines[1:len(lines) - 2]:
            key, value = line.split(': ')
            headers[key] = value

        return Request(method, target, http_version, headers)
