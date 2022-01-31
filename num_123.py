'''초보자를 위한 파이썬 300제
사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
각 통화별 환율은 다음과 같다.
사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
통화명	환율
달러	1167
엔	1.096
유로	1268
위안	171'''
money = ['달러', '엔', '유로', '위안']
data = input('입력:')
tokens = data.split()
amount = int(tokens[0])
currency = tokens[1]
if currency in money[0]:
    print(amount *1167, '원')
elif currency in money[1]:
    print(amount *1.096, '원')
elif currency in money[2]:
    print(amount *1268, '원')
else:
    print(amount *171, '원')