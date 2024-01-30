from dataclasses import dataclass

from dataclasses_json import dataclass_json

from data_objects.customer import Customer
from data_objects.demands.demands import Demands
from data_objects.product import Product


@dataclass_json
@dataclass
class Order:
    id: str
    customer: Customer
    demands: Demands 
    products: list[Product]
