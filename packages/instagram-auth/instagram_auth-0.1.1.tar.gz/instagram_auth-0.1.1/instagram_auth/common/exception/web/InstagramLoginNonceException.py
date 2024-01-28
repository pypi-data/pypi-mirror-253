__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "14.01.2024 05:00"

from instagram_auth.common.exception.web.ResponseException import ResponseException


class InstagramLoginNonceException(ResponseException):
    """ Ошибка в получении login_nonce токена """
    pass
