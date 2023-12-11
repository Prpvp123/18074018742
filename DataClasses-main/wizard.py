from dataclasses import dataclass


@dataclass(order=True)
class Wizard:
    name: str
    rating: int
    age: int

    def change_rating(self, value):
        new_rating = max(1, min(100, self.rating + value))
        new_age = abs(value) // 10

        self.age = max(18,
                       self.age - new_age) if value > 0 else self.age + new_age

        self.rating = new_rating

    def __iadd__(self, wd: str):
        self.rating += len(wd)
        self.age -= len(wd) // 10

        return self

    def __call__(self, num: int):
        return (num - self.age) * self.rating

    def __str__(self):
        return (f"Wizard {self.name} with {self.rating} rating looks "
                f"{self.age} years old")


wizard1 = Wizard("Merlin", 10, 100)
print(wizard1)

wizard2 = Wizard("Gandalf", 15, 150)
print(wizard2)

wizard1 += "magic"
wizard1.change_rating(20)
print(wizard1)
result = wizard1(5)
print(result)

print(wizard1 < wizard2)
print(wizard1 > wizard2)
print(wizard1 <= wizard2)
print(wizard1 >= wizard2)
print(wizard1 == wizard2)
print(wizard1 != wizard2)
