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

    async def get(self, id_: int = None):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='account',
        )
        return response

    async def search(self, id_: int = None, username: str = None, page: int = None):
        path = '/search'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'username': username,
                'page': page,
            },
            response_key='',
        )
        return response

    async def create_service(self, account_id: int, service: str, answers: str):
        path = '/services/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'account_id': account_id,
                'service': service,
                'answers': answers,
            },
            response_key='id',
        )
        return response

    async def update_service(
            self,
            id_: int,
            answers: str,
            state: str,
            datetime_from: str,
            datetime_to: str,
    ):
        path = '/services/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_': id_,
                'answers': answers,
                'state': state,
                'datetime_from': datetime_from,
                'datetime_to': datetime_to,
            },
        )
        return response

    async def delete_service(self, id_: int):
        path = '/services/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_': id_,
            },
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

    async def get_list_roles(self):
        path = '/roles/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='roles',
        )
        return response

    async def get_role(self, account_id: int):
        path = '/roles/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'account_id': account_id
            },
            response_key='accounts_roles',
        )
        return response

    async def create_role(self, account_id: int, role_id: int):
        path = '/roles/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'account_id': account_id,
                'role_id': role_id,
            },
            response_key='id',
        )
        return response

    async def delete_role(self, id_: int):
        path = '/roles/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
