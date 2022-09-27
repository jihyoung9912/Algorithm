class Person:
    def __init__(self, name = '', age = 0, salary=0.0):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'{self.name}, {self.age}, {self.salary}'

p1 = Person()
p1.name = "James"; p1.age = 20; p1.salary = 100.0
p2 = Person()
p2.name = "Edward"; p2.age = 21
print(p1)
print(p2)
