__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "14.01.2024 04:58"

from instagram_auth.common.exception.web.ResponseException import ResponseException


class CSRFTokenException(ResponseException):
    pass
