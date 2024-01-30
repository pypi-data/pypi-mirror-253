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


class Service(BaseSection):
    prefix = 'services'

    async def create(self, id_str: str, name: str, questions: str):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_str': id_str,
                'name': name,
                'questions': questions,
            },
            response_key='id_str',
        )
        return response

    async def update(self, id_str: str, name: str = None, questions: str = None):
        path = '/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_str': id_str,
                'name': name,
                'questions': questions,
            },
        )
        return response

    async def delete(self, id_str: str):
        path = '/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_str': id_str,
            },
        )
        return response

    async def create_cost(self, service: str, currency: str, cost: float):
        path = '/costs/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'service': service,
                'currency': currency,
                'cost': cost,
            },
            response_key='id',
        )
        return response

    async def update_cost(self, id_: int, cost: float):
        path = '/costs/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id_': id_,
                'cost': cost,
            },
        )
        return response

    async def delete_cost(self, id_: int):
        path = '/costs/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
