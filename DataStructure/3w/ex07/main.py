from element import Element

size = 10
list_ = [0] * size
print(list_)

list_ = [Element(10)] * size
print(list_)

list_[0].num = 99
print(list_)