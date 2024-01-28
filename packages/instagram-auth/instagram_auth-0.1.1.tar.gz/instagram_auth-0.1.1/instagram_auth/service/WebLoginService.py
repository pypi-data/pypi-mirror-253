__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "13.01.2024 06:59"

from urllib.parse import unquote

import aiohttp
from aiohttp import ClientSession

from instagram_auth.common.PasswordUtils import PasswordUtils
from instagram_auth.common.exception.web.CSRFTokenException import CSRFTokenException
from instagram_auth.common.exception.web.InstagramLoginNonceException import InstagramLoginNonceException
from instagram_auth.common.exception.web.InstagramSignInException import InstagramSignInException
from instagram_auth.common.model.InstagramShortUser import InstagramShortUser


class WebLoginService:

    DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Ig-App-Id": "936619743392459",
        "X-Instagram-Ajax": "1010801225",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.instagram.com",
        "Viewport-Width": "1728",
        "dpr": "1"
    }

    DEFAULT_COOKIES = {
        "ig_did": "183D0C6A-2A2F-4D13-ACAB-1F699F93BDEA",
        "datr": "blCgZXM302jOB7BO4tR4nZqY",
        "mid": "ZaBXswAEAAGylo7iozvu4FDXWmPn",
        "ig_nrcb": 1
    }

    def __init__(self, session: ClientSession | None = None, default_cookies: dict = None, default_headers: dict = None):
        self.session = session
        if default_cookies is not None:
            self.DEFAULT_COOKIES = default_cookies
        if default_headers is not None:
            self.DEFAULT_HEADERS = default_headers

    async def login(self, username, password) -> (InstagramShortUser, str):
        """
        :return: (user_info_model, sessionid)
        """
        if username == "" or password == "":
            raise InstagramSignInException("Username and Password is required to be not empty")
        headers = self.DEFAULT_HEADERS.copy()
        async with self.session or aiohttp.ClientSession(headers=headers, raise_for_status=False) as session:
            password_utils = PasswordUtils()
            url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
            data = {
                "username": username,
                "enc_password": await password_utils.encrypt(password),
                "optIntoOneTap": False,
                "queryParams": {},
                "trustedDeviceRecords": {}
            }
            headers, cookies = await self.__build_headers_and_cookies(session=session, headers=headers)
            # TODO add certificate for 'www.instagram.com' to client/system
            async with session.post(url, data=data, ssl=False, headers=headers, cookies=cookies) as response:
                if response.status == 200:
                    response_data: dict = await response.json()
                    if response_data.get("authenticated", False):
                        return InstagramShortUser(**response_data), unquote(response.cookies.get("sessionid").value)
                    else:
                        raise InstagramSignInException(f"Error on sign in. Maybe wrong password", response)
                else:
                    raise InstagramSignInException(f"Error on sign in", response)

    async def reissue_session_id(self, sessionid: str, user_id: str, login_nonce: str | None = None) -> (str, str):
        """
        Перевыпустить sessionid

        :param sessionid:
        :param user_id:
        :param login_nonce: если есть, то можно использовать. Иначе будет выпущен новый
        :return: (new_login_nonce, new_session_id)
        """
        headers = self.DEFAULT_HEADERS.copy()
        url = "https://www.instagram.com/api/v1/web/accounts/one_tap_web_login/"
        async with aiohttp.ClientSession(headers=headers, raise_for_status=False) as session:
            if login_nonce is None:
                login_nonce = await self.login_nonce(session, sessionid)
            headers, cookies = await self.__build_headers_and_cookies(session=session, sessionid=sessionid, headers=headers)
            body = {
                "login_nonce": login_nonce,
                "queryParams": {},
                "trustedDeviceRecords": {},
                "user_id": user_id
            }
            async with session.post(url, data=body, headers=headers, cookies=cookies) as response:
                if response.status == 200 and response.content_type == "application/json":
                    data = await response.json()
                    if data.get("authenticated", False):
                        new_login_nonce: str | None = data.get("login_nonce", None)
                        new_sessionid = response.cookies.get("sessionid", None)
                        if new_login_nonce is not None or new_sessionid is not None:
                            return new_login_nonce, new_sessionid.value
                else:
                    return None

    @classmethod
    async def login_nonce(cls, session: ClientSession, sessionid: str) -> str | None:
        headers, cookies = await cls.__build_headers_and_cookies(session=session, sessionid=sessionid)
        url = "https://www.instagram.com/api/v1/web/accounts/request_one_tap_login_nonce/"
        async with session.post(url, headers=headers, cookies=cookies) as response:
            if response.status == 200 and response.content_type == "application/json":
                data: dict = await response.json()
                return data.get("login_nonce", None)
            else:
                raise InstagramLoginNonceException(f"Error on get login nonce", response)

    @staticmethod
    async def csrf_token(session) -> str:
        url = "https://www.instagram.com/data/shared_data/"
        async with session.get(url, ssl=False) as response:
            if response.status == 200 and response.content_type == "application/json":
                data = await response.json()
                config: dict = data.get("config", {})
                csrf_token: str | None = config.get("csrf_token", None)
                if csrf_token is not None:
                    return csrf_token
                else:
                    raise CSRFTokenException(f"Error on get csrftoken", response)
            else:
                raise CSRFTokenException(f"error on get csrftoken", response)

    @classmethod
    async def csrf_token_header(cls, session: ClientSession) -> (dict, str):
        """
        :return: (csrf_header, csrf_token)
        """
        csrf_token = await cls.csrf_token(session)
        if csrf_token is not None:
            return {
                "X-Csrftoken": csrf_token
            }, csrf_token
        else:
            raise CSRFTokenException("Error on get csrf_token. Reason: csrf_token is None")

    @classmethod
    async def __build_headers_and_cookies(
            cls,
            session: ClientSession,
            sessionid: str | None = None,
            headers: dict | None = None,
            cookies: dict | None = None
    ) -> (dict, dict):
        """
        :return: (headers, cookies)
        """
        csrf_header, csrf_token = await cls.csrf_token_header(session)
        if headers is None:
            headers = cls.DEFAULT_HEADERS.copy()
        headers.update(csrf_header)
        if cookies is None:
            cookies = cls.DEFAULT_COOKIES.copy()
        cookies.update(
            {
                "csrftoken": csrf_token,
            }
        )
        if sessionid is not None:
            cookies.update({"sessionid": sessionid})
        return headers, cookies
