__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "14.01.2024 04:50"

from aiohttp import ClientResponse


class ResponseException(Exception):

    def __init__(self, message: str, response: ClientResponse | None = None):
        super().__init__(self)
        self.response = response
        self.message = message

    def __str__(self):
        if self.response is not None:
            return f"{self.message}. \nResponse: status={self.response.status}, headers={self.response.headers}, \ncookies={self.response.cookies}"
        else:
            return f"{self.message}"
