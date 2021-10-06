class Person:
    def __init__(self, age):
        self.__age = age
    def get_age(self):
        return self.age
a = Person(4)
print(a.age)