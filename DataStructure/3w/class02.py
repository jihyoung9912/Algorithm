class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name is: {self.name}, {self.age}"

st = Student("JiHyeong", 24)
print(st)