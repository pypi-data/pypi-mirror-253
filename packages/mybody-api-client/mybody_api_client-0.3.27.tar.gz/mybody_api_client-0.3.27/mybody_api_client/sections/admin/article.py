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


class Article(BaseSection):
    prefix = 'articles'

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

    async def update(self, id_: int, is_hide: bool = None):
        path = '/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'is_hide': is_hide,
            },
        )
        return response

    async def update_md(self, id_: int, md: str, language: str = None):
        path = '/md/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'language': language,
                'md': md,
            },
        )
        return response

    async def create_translation(self, id_: int, language: str, name: None):
        path = '/translations/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'article_id': id_,
                'language': language,
                'name': name,
            },
            response_key='id',
        )
        return response

    async def delete_translation(self, id_: int, language: str):
        path = '/translations/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'article_id': id_,
                'language': language,
            },
        )
        return response
