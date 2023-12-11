from dataclasses import dataclass, field
from typing import Any
from random import randint


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


class GoodsMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0, 0, 0]


@dataclass
class Book(Goods):
    title: str
    auth: str
    price: int
    weight: float | int
    meassure: list = field(
        default_factory=GoodsMeassureFactory.get_init_meassure)


b = Book(1000, 1.2, 'Harry Potter', 'kmjnhbgfd')
print(b)
g = Goods('87654321234567', 1200)
print(g)
g2 = Goods('87654321234567', 1200)
print(g)
b2 = Book(2000, 2.5, 'jnbhgvfv', 'l,kmjnhg')
for i in range(len(b2.meassure)):
    b.meassure[1] = randint(10, 20)
print(b2)
