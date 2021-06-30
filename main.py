#Object oriented programming exercise

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def bark(self):
        return 'Wouff'

    def text(self):
        return f'My doggy name is {self.name} and I say wuf wuf, and I am {self.age} years old!'


d = Dog("Boy", 10)
print(d)

print(d.text())

print(type(d))


