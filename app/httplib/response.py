from .constants import CRLF, HTTP_VERSION, TEXT_ENCODING


class Response:
    @staticmethod
    def send_request(messages: list[str], n_crlf = 2) -> bytes:
        message = HTTP_VERSION + ' ' + CRLF.join(messages) + (CRLF * n_crlf)
        return message.encode(TEXT_ENCODING)
