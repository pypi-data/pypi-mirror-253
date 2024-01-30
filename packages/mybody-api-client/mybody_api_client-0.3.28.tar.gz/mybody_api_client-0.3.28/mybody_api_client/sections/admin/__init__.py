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


from .account import Account
from .article import Article
from .country import Country
from .currency import Currency
from .language import Language
from .role import Role
from .service import Service
from .text import Text
from .timezone import Timezone
from .product import Product
from .training import Training
from .exercise import Exercise
from .permission import Permission
from .meal import Meal
from ...utils import BaseCatalog


class Admin(BaseCatalog):
    prefix = 'admin'

    account: Account
    article: Article
    country: Country
    currency: Currency
    language: Language
    role: Role
    service: Service
    text: Text
    timezone: Timezone
    product: Product
    training: Training
    exercise: Exercise
    permission: Permission
    meal: Meal

    sections = [
        Account, Article, Country, Currency, Language,
        Role, Service,
        Text, Timezone, Product, Training, Exercise,
        Permission, Meal,
    ]
