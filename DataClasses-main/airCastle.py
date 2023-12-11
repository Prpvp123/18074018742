from dataclasses import dataclass


@dataclass(order=True)
class AirCastle:
    height: int
    blocks: int
    color: str

    def chang_height(self, value):
        self.height = value if value > -1 else 0

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('Ты шо дурачок?')
        self.blocks = self.blocks + other
        self.height = self.height + other

        return AirCastle(self.height, self.blocks, self.color)

    def invisible(self, visible):
        return f'видимость замка: {self.height // visible * self.blocks}'

    def __str__(self):
        return (f'the aircastle an altude {self.height} meters is {self.color},'
                f' width {self.blocks} clouds')


v = AirCastle(552, 552, 'red')
print(v)
v += 10
print(v)
print(v.invisible(1))
v1 = AirCastle(552, 442, 'blue')
v2 = AirCastle(552, 442, 'blue')
print(v1)
print(v1 < v2)
print(v1 > v2)
print(v1 >= v2)
print(v1 <= v2)
print(v1 != v2)
print(v1 == v2)
