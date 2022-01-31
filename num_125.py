'''초보자를 위한 파이썬 300제
휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
번호	통신사
011	SKT
016	KT
019	LGU
010	알수없음
>> 휴대전화 번호 입력: 011-345-1922
당신은 SKT 사용자입니다.
'''
number = input('휴대전화 번호 입력:')
data = number[:3]

if data == '011':
    comp = 'skt'
elif data == '016':
    comp = 'kt'
elif data == ' 019':
    comp = 'lgu'
else:
    comp = '알수없음'
print(f'당신은 {comp} 사용자입니다.')