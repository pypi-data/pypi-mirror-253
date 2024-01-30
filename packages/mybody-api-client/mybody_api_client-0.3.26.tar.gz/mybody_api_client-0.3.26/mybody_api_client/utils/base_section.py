#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from aiohttp import ClientSession
from addict import Dict
from furl import furl


HOST = 'api.mybody.one'
HOST_TEST = 'api.test.mybody.one'


class RequestTypes:
    GET = 'get'
    POST = 'post'


class ApiException(Exception):
    pass


class BaseSection:
    prefix: str = ''
    token: str

    def __init__(self, token: str = None, is_test: bool = False):
        self.token = token
        self.is_test = is_test

    async def create_url(self, path: str, parameters: dict) -> str:
        f = furl(scheme='https', netloc=HOST_TEST if self.is_test else HOST, path=self.prefix + path)
        f.set(args=parameters)
        return f.url

    async def request(
            self,
            path: str,
            type_: str = RequestTypes.GET,
            token_required: bool = True,
            parameters: dict = None,
            response_key: str = None,
    ):
        parameters = parameters or {}
        json = {}
        if (token_required and self.token) or self.token:
            parameters['token'] = self.token

        if type_ == RequestTypes.POST:
            json = parameters
            parameters = {}

        url = await self.create_url(
            path=path,
            parameters=parameters,
        )

        async with ClientSession() as session:

            if type_ == RequestTypes.GET:
                response = await session.get(url=url)
            elif type_ == RequestTypes.POST:
                response = await session.post(url=url, json=json)

        response_json = await response.json()
        response = Dict(**response_json)

        if response.state == 'successful':
            if response_key:
                response = response.get(response_key)

            return response
        elif response.state == 'error':
            raise ApiException(response.message)
