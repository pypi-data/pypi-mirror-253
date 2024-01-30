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


class Meal(BaseSection):
    prefix = 'meals'

    async def get(self, id_: int):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='meal',
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
            response_key='meals',
        )
        return response

    async def get_list_all(self):
        path = '/list/get/all'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='meals',
        )
        return response

    async def create(
            self,
            account_service_id: int,
            date: str,
            type_: str,
            fats: int,
            proteins: int,
            carbohydrates: int,
    ):
        path = '/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'account_service_id': account_service_id,
                'date': date,
                'type': type_,
                'fats': fats,
                'proteins': proteins,
                'carbohydrates': carbohydrates,
            },
            response_key='id',
        )
        return response

    async def update(
            self,
            id_: int,
            date: str,
            type_: str,
            fats: int,
            proteins: int,
            carbohydrates: int,
    ):
        path = '/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'date': date,
                'type': type_,
                'fats': fats,
                'proteins': proteins,
                'carbohydrates': carbohydrates,
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

    async def get_product(self, id_: int):
        path = '/products/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='meal_product',
        )
        return response

    async def get_list_products(self):
        path = '/products/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            response_key='meal_products',
        )
        return response

    async def create_product(self, meal_id: int, product_id: int, value: int):
        path = '/products/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'meal_id': meal_id,
                'product_id': product_id,
                'value': value
            },
            response_key='id',
        )
        return response

    async def update_product(self, id_: int, product_id: int, value: int):
        path = '/products/update'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
                'product_id': product_id,
                'value': value
            },
        )
        return response

    async def delete_product(self, id_: int):
        path = '/products/delete'
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
            response_key='report',
        )
        return response

    async def create_report(
            self,
            meal_id: int,
            comment: str,
            images,
            products,
    ):
        path = '/reports/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'meal_id': meal_id,
                'comment': comment,
                'images': images,
                'products': products,
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

    async def get_list_images_reports(self, meal_report_id: int):
        path = 'reports/images/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'meal_report_id': meal_report_id,
            },
        )
        return response

    async def create_image_report(
            self,
            meal_report_id: int,
            image: str,
    ):
        path = '/reports/images/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'meal_report_id': meal_report_id,
                'image': image,
            },
            response_key='id',
        )
        return response

    async def delete_image_report(self, id_: int):
        path = '/reports/images/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response

    async def get_list_product_reports(self, meal_report_id: int):
        path = 'reports/products/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'meal_report_id': meal_report_id,
            },
            response_key='meal_report_products',
        )
        return response

    async def create_product_report(
            self,
            meal_report_id: int,
            product_id: int,
            value: int,
    ):
        path = '/reports/products/create'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'meal_report_id': meal_report_id,
                'product_id': product_id,
                'value': value,
            },
            response_key='id',
        )
        return response

    async def delete_product_report(self, id_: int):
        path = '/reports/products/delete'
        response = await self.request(
            type_=RequestTypes.POST,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response
