class Pet:
    def __init__(self, name, age, master, height, weight):
        self.name = name
        self.age = age
        self.master = master
        self.height = height
        self.weight = weight

    def run(self):
        return f'{self.name} is running'

    def jump(self):
        return f'{self.name} is jumping'

    def birthday(self):
        self.age += 1

    def sleep(self):
        return f'{self.name} is sleeping'


class Dog(Pet):
    def bark(self):
        return f'{self.name} is barking'


class Cat(Pet):
    def meow(self):
        return f'{self.name} is meowing'


class Parrot(Pet):
    def fly(self):
        return f'{self.name} is flying'


dog = Dog('Max', 5, 'Jon', 50, 10)
print(dog.run())
print(dog.jump())
dog.birthday()
print(f'{dog.name} age {dog.age}')
print(dog.sleep())
print(dog.bark())

cat = Cat('Felix', 3, 'Alice', 20, 6)
print(cat.run())
print(cat.jump())
cat.birthday()
print(f'{cat.name} age {cat.age}')
print(cat.sleep())
print(cat.meow())

parrot = Parrot('Ruby', 1, 'Oliver', 10, 1)
print(parrot.run())
print(parrot.jump())
parrot.birthday()
print(f'{parrot.name} age {parrot.age}')
print(parrot.sleep())
print(parrot.fly())
