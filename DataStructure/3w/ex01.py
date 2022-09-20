class Element:
    def __init__(self, num=0):
        self.num = num

    def __str__(self): #클래스를 print 했을 때의 출력 값 str, repr이 동시에 존재할 경우 str로 호출됨
        #str 함수를 먼저 찾고, 없으면 repr을 찾는다
        return f"Element:{self.num}"

    def __repr__(self): #객체에 이름을 지어준다.  메모리값을 표현해주는 함수
        return str(self)

elem = [Element(100), Element(200)]
print(elem)