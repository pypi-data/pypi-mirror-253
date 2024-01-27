#!/usr/bin/env python3

import os
from typing import Optional, Union, Any, Dict, Type, List
from dataclasses import dataclass
from .endpoints import (
    TasksEndpoint,
    ExtensionsEndpoint
)

from .errors import (
    RequestTimeoutError,
    is_api_error_code,
    APIResponseError,
    HTTPResponseError
)
from types import TracebackType
from abc import abstractclassmethod
import httpx
from httpx import Request, Response
from .typing import SyncAsync


@dataclass
class ClientOptions:
    auth: Optional[str] = None
    timeout_ms: int = 60_000
    base_url: str = "https://api.dida365.com/api/v2"
    user_agent: str = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'



class BaseClient:

    def __init__(self,
                 cookie: str,
                 client: Union[httpx.Client, httpx.AsyncClient],
            ) -> None:
        
        self.cookie = cookie

        self.options = ClientOptions()

        self._clients: List[Union[httpx.Client, httpx.AsyncClient]] = []
        self.client = client

        self.task = TasksEndpoint(self)
        self.extensions = ExtensionsEndpoint(self)
    
    @property
    def client(self) -> Union[httpx.Client, httpx.AsyncClient]:
        return self._clients[-1]
    
    @client.setter
    def client(self, client: Union[httpx.Client, httpx.AsyncClient]) -> None:
        client.base_url = httpx.URL(f'{self.options.base_url}/')
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        client.headers = httpx.Headers(
            {
                "User-Agent": self.options.user_agent,
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': self.cookie
            }
        )
        self._clients.append(client)


    def _build_request(self,
                       method: str,
                       path: str,
                       query: Optional[Dict[Any, Any]] = None,
                       body: Optional[Dict[Any, Any]] = None,
                       token: Optional[str] = None) -> Request:
        
        headers = httpx.Headers()
        headers['Authorization'] = f'Bearer {token}'

        return self.client.build_request(
            method=method, url=path, params=query, json=body, headers=headers
        )

    def _parse_response(self, response) -> Any:
        return response.json()
    
    @abstractclassmethod
    def request(self,
                path: str,
                method: str,
                query: Optional[Dict[Any, Any]] = None,
                body: Optional[Dict[Any, Any]] = None,
                auth: Optional[str] = None,
                ) -> SyncAsync[Any]:
        pass


class Client(BaseClient):

    client: httpx.Client

    def __init__(self,
                 cookie: str,
                 client: Optional[httpx.Client]=None) -> None:
        
        if client is None:
            client = httpx.Client()
        super().__init__(cookie, client)
    
    def __enter__(self) -> "Client":
        self.client = httpx.Client()
        self.client.__enter__()
        return self
    
    def __exit__(self,
                 exc_type: Type[BaseException],
                 exc_value: BaseException,
                 traceback: TracebackType) -> None:
        self.client.__exit__(exc_type, exc_value, traceback)
        del self._clients[-1]
    
    def close(self) -> None:
        self.client.close()


    def request(self,
                path: str,
                method: str,
                query: Optional[Dict[Any, Any]] = None,
                body: Optional[Dict[Any, Any]] = None,
                token: Optional[str] = None,
                ) -> Any:

        request = self._build_request(method, path, query, body)
        
        try:
            return self._parse_response(self.client.send(request))
        except httpx.TimeoutException:
            raise RequestTimeoutError()




