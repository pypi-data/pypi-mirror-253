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


class Training(BaseSection):
    prefix = 'trainings'

    async def get(self, id_: int):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='training',
        )
        return response

    async def get_list(self, account_service_id: int, date: str = None):
        path = '/list/get'
        parameters = {'account_service_id': account_service_id}
        if date is not None:
            parameters['date'] = date
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters=parameters,
            response_key='trainings',
        )
        return response

    async def get_list_all(self):
        path = '/list/get/all'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='trainings',
        )
        return response

    async def create(self, account_service_id: int, date: str, article_id: int = None):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'account_service_id': account_service_id,
                'date': date,
                'article_id': article_id,
            },
            response_key='id',
        )
        return response

    async def update(self, id_: int, date: str = None, article_id: int = None):
        path = '/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'date': date,
                'article_id': article_id,
            },
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

    async def get_exercise(self, id_: int):
        path = '/exercises/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='training_exercise',
        )
        return response

    async def get_list_exercises(self, training_id: int):
        path = '/exercises/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'training_id': training_id,
            },
            response_key='training_exercises',
        )
        return response

    async def create_exercise(
            self,
            training_id: int,
            exercise_id: int,
            priority: int,
            value: int,
            rest: int,
    ):
        path = '/exercises/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'training_id': training_id,
                'exercise_id': exercise_id,
                'priority': priority,
                'value': value,
                'rest': rest,
            },
            response_key='id',
        )
        return response

    async def update_exercise(
            self,
            id_: int,
            exercise_id: int = None,
            priority: int = None,
            value: int = None,
            rest: int = None,
    ):
        path = '/exercises/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'exercise_id': exercise_id,
                'priority': priority,
                'value': value,
                'rest': rest,
            },
        )
        return response

    async def delete_exercise(self, id_: int):
        path = '/exercises/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response

    async def get_report(self, id_: int):
        path = '/reports/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='training_report',
        )
        return response

    async def get_list_reports(self):
        path = '/reports/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='training_reports',
        )
        return response

    async def create_report(self, training_id: int, comment: str):
        path = '/reports/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'training_id': training_id,
                'comment': comment,
            },
            response_key='id',
        )
        return response

    async def delete_report(self, id_: int):
        path = '/reports/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
