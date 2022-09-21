class Person:
    def __init__(self, name='', age=0, salary=0.0):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'{self.name}, {self.age}, {self.salary}'



print(Person('James', 20, 100.0))
print(Person('Edward', 21, 0.0))