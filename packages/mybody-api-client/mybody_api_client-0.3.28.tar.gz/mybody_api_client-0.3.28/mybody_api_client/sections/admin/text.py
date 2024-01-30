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


class Text(BaseSection):
    prefix = 'texts'

    async def create(self, key: str, value_default: str):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'key': key,
                'value_default': value_default,
            },
            response_key='key',
        )
        return response

    async def get(self, key: str):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'key': key,
            },
            response_key='text',
        )
        return response

    async def get_list(self):
        path = '/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='texts',
        )
        return response

    async def update(self, key: str, value_default: str = None, new_key: str = None):
        path = '/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'key': key,
                'value_default': value_default,
                'new_key': new_key,
            },
        )
        return response

    async def delete(self, key: str):
        path = '/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'key': key,
            },
        )
        return response

    async def create_translation(self, text_key: str, language: str, value: str):
        path = '/translations/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'text_key': text_key,
                'language': language,
                'value': value,
            },
            response_key='id',
        )
        return response

    async def update_translation(self, text_key: str, language: str, value: str):
        path = '/translations/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'text_key': text_key,
                'language': language,
                'value': value,
            },
        )
        return response

    async def delete_translation(self, text_key: str, language: str):
        path = '/translations/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'text_key': text_key,
                'language': language,
            },
        )
        return response

    async def create_pack(self, language: str):
        path = '/packs/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'language': language,
            },
            response_key='id',
        )
        return response

    async def delete_pack(self, id_: int):
        path = '/packs/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
