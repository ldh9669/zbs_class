'''초보자를 위한 파이썬 300제
사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
>> input number1: 10
>> input number2: 9
>> input number3: 20
20'''
a = int(input('number1:'))
b = int(input('number2:'))
c = int(input('number3:'))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)