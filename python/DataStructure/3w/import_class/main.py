from element import Element
from elements import Elements

# elems = Elements()
# elems[0] = Element(10)
# elems[3] = Element(20)
# print(elems)

size = 10

list_ = [0] * size
print(list_)

list_01 = [Element(10)] * size
print(list_01)
list_01[0].elem = 99
print(list_01)
# Element(10)이라는 같은 값을 참조하여 생성되기 때문에 한 값만 바꿔도 전체가 해당 값으로 변경. 같은 주소를 참조하기 때문

list_ = [Element(10) for _ in range(size)]
list_[0].elem = 99
print(list_)
# 반복문으로 서로 같은 주소를 참조하지 않는 list_로 만들어 변경
