import asyncio
from typing import Optional, Callable
from httpx import AsyncClient
from requests_oauthlib import OAuth2Session
from async_oauthlib import OAuth2Session as AsyncOAuth2Session
import requests
from .RequestException import EtsyRequestException
from etsy_apiv3.models import Me


class EtsySession:

    def __token_updater(self, token):
        return token

    async def __async_token_saver(self, token):
        return token
    
    def __init__(self,
                 client_key: str,
                 client_secret: str,
                 token: Optional[dict] = None,
                 token_updater: Optional[Callable] = None
                 ):

        self.CLIENT_KEY = client_key
        self.CLIENT_SECRET = client_secret
        self.__base_endpoint = "https://openapi.etsy.com/v3/application/"
        self.__oauth2_session = None
        
        if token is not None:
            if token_updater is None:
                self.token_updater = self.__token_updater
            else:
                self.token_updater = token_updater
            self.TOKEN = token
            
            self.__refresh_url = "https://api.etsy.com/v3/public/oauth/token"
            self.__oauth2_session = self.__create_oath2_session()
            
            self.__me = None
            
        else:
            self.__oauth2_session = requests.Session()

    def __create_oath2_session(self) -> OAuth2Session:
        refresh_kwargs = {
            'client_id': self.CLIENT_KEY,
            'client_secret': self.CLIENT_SECRET,
        }

        session = OAuth2Session(self.CLIENT_KEY, token=self.TOKEN, auto_refresh_kwargs=refresh_kwargs,
                                auto_refresh_url=self.__refresh_url, token_updater=self.token_updater
                                )
        return session
    
    def create_async_oauth2_session(self) -> AsyncOAuth2Session:
        refresh_kwargs = {
        'client_id': self.CLIENT_KEY,
        'client_secret': self.CLIENT_SECRET,
        }
        session = AsyncOAuth2Session(self.CLIENT_KEY, token=self.TOKEN, auto_refresh_kwargs=refresh_kwargs,
            auto_refresh_url=self.__refresh_url, token_updater=self.__async_token_saver
        )
        return session
    
    @property
    def me(self) -> Me:
        if self.__me is None:
            self.__me = Me(**self.request(f"users/me"))
        return self.__me
    
    @staticmethod
    def create_response(response: requests.Response):
        json: dict = response.json()

        if "error" in json.keys():
            raise EtsyRequestException(response.status_code, json["error"])
        
        return json

    def request(self, endpoint: str, method="GET", headers: Optional[dict] = None, *args, **kwargs) -> dict:
        """ 
        Send Request to target endpoint by method

        Args:
            endpoint (str): Api Endpoint Url
            method (str, optional): HTTP Methods [GET, POST, PUT, DELETE, UPDATE]. Defaults to "GET".

        Raises:
            EtsyRequestException: EtsyRequestException(status_code, message)

        Returns:
            json: Json From Request Response
        """
        if headers is None:
            headers = {"x-api-key": self.CLIENT_KEY}

        url = f"{self.__base_endpoint}{endpoint}"
        req = self.__oauth2_session.request(
            method, url, headers=headers, *args, **kwargs)

        return self.create_response(req)

    async def async_request(self, endpoint: str,  session: AsyncOAuth2Session = None, method="GET", headers: Optional[dict] = None, *args, **kwargs) -> dict:
        
        url = f"{self.__base_endpoint}{endpoint}"
        
        if headers is None:
            headers = {"x-api-key": self.CLIENT_KEY}
        
        res = await session.get(url=url, headers=headers, *args, **kwargs)
        json = await res.json()
        if "error" in json.keys():
            raise EtsyRequestException(res.status, json["error"])
        return json
