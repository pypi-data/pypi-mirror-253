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


from mybody_api_client.utils.base_section import BaseSection, RequestTypes


class Account(BaseSection):
    prefix = 'accounts'

    async def get(self):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='account',
        )
        return response

    async def create(
            self,
            username: str,
            password: str,
            firstname: str,
            lastname: str,
            country: str,
            language: str,
            timezone: str,
            currency: str,
            surname: str = None,
    ):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            token_required=False,
            parameters={
                'username': username,
                'password': password,
                'firstname': firstname,
                'lastname': lastname,
                'surname': surname,
                'country': country,
                'language': language,
                'timezone': timezone,
                'currency': currency,
            },
            response_key='id',
        )
        return response

    async def check_username(self, username: str):
        path = '/username/check'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
                'username': username,
            }
        )
        return response

    async def get_service(self, id_: int):
        path = '/services/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='account_service',
        )
        return response

    async def get_list_services(self):
        path = '/services/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='account_services',
        )
        return response

    async def create_service(self, service: str, answers: str):
        path = '/services/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'service': service,
                'answers': answers,
            },
            response_key='id',
        )
        return response
