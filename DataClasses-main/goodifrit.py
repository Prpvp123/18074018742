from dataclasses import dataclass


@dataclass(order=True)
class GoodIfrit:
    height: int
    name: str
    goodness: int = 0

    def change_goodness(self, value):
        self.goodness = max(0, self.goodness + value)

    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.goodness)

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return (f"Good Ifrit {self.name}, height {self.height}, goodness"
                f" {self.goodness}")


gi1 = GoodIfrit(10, "Ifrit1", 5)
print(gi1)

gi1.change_goodness(3)
print(gi1)

gi2 = gi1 + 9
print(gi2)

result = gi2(10)
print(result)

gi3 = GoodIfrit(10, "Ifrit2", 8)
print(gi1 < gi3)
print(gi1 > gi3)
print(gi1 <= gi3)
print(gi1 >= gi3)
print(gi1 == gi3)
print(gi1 != gi3)

gi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness(4)
print(gi)
gi1 = gi + 15
print(gi1)
print(gi(31))

gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')
