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

    async def get(self, id_: int):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
              'id': id_,
            },
            response_key='role',
        )
        return response

    async def get_list(self):
        path = '/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            response_key='roles',
        )
        return response

    async def get_permission(self, id_: int):
        path = '/permissions/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
              'id': id_,
            },
            response_key='role_permission',
        )
        return response

    async def get_list_permissions(self, role_id: int):
        path = '/permissions/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
                'role_id': role_id,
            },
            response_key='role_permissions',
        )
        return response
