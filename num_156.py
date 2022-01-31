'''초보자를 위한 파이썬 300제
리스트에서 소문자만 화면에 출력하라.

리스트 = ["A", "b", "c", "D"]
b
c'''

리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper() == False:
        print(i)