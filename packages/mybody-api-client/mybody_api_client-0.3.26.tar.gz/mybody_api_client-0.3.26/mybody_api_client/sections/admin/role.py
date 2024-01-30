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


from mybody_api_client.utils.base_section import RequestTypes, BaseSection


class Role(BaseSection):
    prefix = 'roles'

    async def create(self, name: str):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
              'name': name,
            },
            response_key='id',
        )
        return response

    async def delete(self, id_: int):
        path = '/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
              'id': id_,
            },
        )
        return response

    async def create_permission(self, role_id: int, permission: str):
        path = '/permissions/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'role_id': role_id,
                'permission': permission,
            },
            response_key='id',
        )
        return response

    async def delete_permission(self, id_: int):
        path = '/permissions/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
