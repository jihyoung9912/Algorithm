v = None
if not v:
    print("Here1")

if v is None:
    print("Here2")

v = 0
if not v:
    print("Here3")
if v is None:
    print("Here4")

str_ = ""
if not str_:
    print("Here5")
#Empty 객체가 있으므로 None이 아니다
if str_ is None:
    print("Here6")
