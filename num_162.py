'''초보자를 위한 파이썬 300제
월드컵은 4년에 한 번 개최된다.
range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

2002
2006
2010
...
2042
2046
2050
참고) range의 세번 째 파라미터는 증감폭을 결정합니다.

>> print(list(range(0, 10, 2)))
[0, 2, 4, 6, 8]'''

for list in range(2002, 2051, 4):
    print(list)