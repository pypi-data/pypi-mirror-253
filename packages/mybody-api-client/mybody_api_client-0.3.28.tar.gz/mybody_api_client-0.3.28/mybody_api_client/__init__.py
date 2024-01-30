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


from .sections import Client, Admin


class MyBodyApiClient:
    client: Client
    admin: Admin

    catalogs = [
        Client,
        Admin,
    ]

    def __init__(self, token: str = None, is_test=False):
        for catalog in self.catalogs:
            exec(f'self.{catalog.__name__.lower()} = catalog(token=token, is_test=is_test)')
