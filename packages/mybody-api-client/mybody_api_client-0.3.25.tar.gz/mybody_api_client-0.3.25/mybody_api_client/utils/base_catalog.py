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


from mybody_api_client.utils.base_section import BaseSection


class BaseCatalog:
    prefix: str = ''
    sections: list[BaseSection]

    def __init__(self, token: str, is_test: bool):
        for section in self.sections:
            exec(f'self.{section.__name__.lower()} = section(token=token, is_test=is_test)')
            if self.prefix:
                exec(
                    f'self.{section.__name__.lower()}.prefix = '
                    f'self.prefix + "/" + self.{section.__name__.lower()}.prefix'
                )
