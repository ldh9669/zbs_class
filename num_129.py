'''초보자를 위한 파이썬 300제
주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

  8 2 1 0 1 0 - 1 6 3 5 2 1 0
x 2 3 4 5 6 7   8 9 2 3 4 5 
-----------------------------
1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
2차 계산: 11 -7 = 4
위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.
즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

>> 주민등록번호: 821010-1635210
유효하지 않은 주민등록번호입니다. 
'''

resident_number = str(input('입력:'))
number1 = (int(resident_number[0]) *2) + (int(resident_number[1]) *3) + (int(resident_number[2]) *4) + \
          (int(resident_number[3]) *5) + (int(resident_number[4]) *6) + (int(resident_number[5]) *7) + \
          (int(resident_number[7]) *8) + (int(resident_number[8]) *9) + (int(resident_number[9]) *2) + \
          (int(resident_number[10]) *3) + (int(resident_number[11]) *4) + (int(resident_number[12]) *5)
number1 = number1 % 11
number1 = 11 - number1
number1 = str(number1)
if number1[-1] == resident_number[-1]:
  print('유효한 주민등록번호입니다.')
else:
  print("유효하지 않은 주민등록번호입니다.")