from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.dims = dims
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'{self.__dict__}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)


th = Thing('name1', 1000, 100)
print(th)
td = ThingData('name2', 1500, 150)
td.dims.append(1000)
print(td)
td2 = ThingData('name2', 1500, 150)
print(td2)
# pprint(ThingData.__dict__)
