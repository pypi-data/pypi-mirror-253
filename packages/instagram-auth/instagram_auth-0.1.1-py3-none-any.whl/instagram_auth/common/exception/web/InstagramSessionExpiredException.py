__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "14.01.2024 04:41"

from instagram_auth.common.exception.web.ResponseException import ResponseException


class InstagramSessionExpiredException(ResponseException):
    pass
