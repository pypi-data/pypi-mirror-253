#!/usr/bin/env python3

import json
from collections import namedtuple
from typing import Optional, Union, Any, Dict, Type, List
from dataclasses import dataclass
from .endpoints import (
    UsersEndpoint,
    DatabasesEndpoint,
    PagesEndpoint,
    BuildEndpoint,
    ExtensionsEndpoint,
    BlocksEndpoint
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
    base_url: str = "https://api.notion.com"
    notion_version: str = "2022-06-28"


class BaseClient:

    def __init__(self,
                 client: Union[httpx.Client, httpx.AsyncClient],
                 options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
                 **kwargs: Any,
            ) -> None:
        if options is None:
            options = ClientOptions(**kwargs)
        elif isinstance(options, dict):
            options = ClientOptions(**options)
        
        self.options = options

        self._clients: List[Union[httpx.Client, httpx.AsyncClient]] = []
        self.client = client

        self.blocks = BlocksEndpoint(self)
        self.users = UsersEndpoint(self)
        self.databases = DatabasesEndpoint(self)
        self.pages = PagesEndpoint(self)
        self.build = BuildEndpoint(self)
        self.extensions = ExtensionsEndpoint(self)
    
    @property
    def client(self) -> Union[httpx.Client, httpx.AsyncClient]:
        return self._clients[-1]
    
    @client.setter
    def client(self, client: Union[httpx.Client, httpx.AsyncClient]) -> None:
        client.base_url = httpx.URL(f'{self.options.base_url}/v1/')
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        client.headers = httpx.Headers(
            {
                "Notion-Version": self.options.notion_version,
            }
        )

        if self.options.auth:
            client.headers['Authorization']= f'Bearer {self.options.auth}'
        self._clients.append(client)


    def _build_request(self,
                       method: str,
                       path: str,
                       query: Optional[Dict[Any, Any]] = None,
                       body: Optional[Dict[Any, Any]] = None,
                       auth: Optional[str] = None) -> Request:
        
        headers = httpx.Headers()
        if auth:
            headers["Authorization"] = f"Bearer {auth}"
        return self.client.build_request(
            method, path, params=query, json=body, headers=headers
        )

    def _parse_response2(self, response) -> Any:
        Resp = namedtuple('Resp', ['object', 'results', 'status', 'code', 'message', 'properties', 'child_page', 'raw'])

        return Resp(object=response.get('object'),
                    results=response.get('results'),
                    status=response.get('status'),
                    code=response.get('code'),
                    message=response.get('message'),
                    properties=response.get('properties'),
                    child_page=response.get('child_page'),
                    raw=response)

    def _parse_response(self, response: Response) -> Any:
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as error:
            try:
                body = error.response.json()
                code = body.get('code')
            except json.JSONDecodeError:
                code = None
            if code and is_api_error_code(code):
                raise APIResponseError(response, body['message'], code)
            raise HTTPResponseError
        
        body = response.json()

        return self._parse_response2(body)

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
                 options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
                 client: Optional[httpx.Client] = None,
                 **kwargs: Any) -> None:
        if client is None:
            client = httpx.Client()
            
        super().__init__(client, options, **kwargs)
    
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
                auth: Optional[str] = None,
                ) -> Any:
        request = self._build_request(method, path, query, body, auth)
        try:
            response = self.client.send(request)
        except httpx.TimeoutException:
            raise RequestTimeoutError()
        
        return self._parse_response(response)



