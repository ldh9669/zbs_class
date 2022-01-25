numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

resultp = 1
resultR = 1
resultC = 1

for n in range(numN, (numN - numR), -1):
    print('n : {}'.format(n))
    resultp = resultp * n

print('resultp : {}'.format(resultp))

for n in range(numR, 0, -1):
    print('n : {}'.format(n))
    resultR = resultR * n

print('resultR : {}'.format(resultR))

resultC = int(resultp / resultR)
print('resultC : {}'.format(resultC))

result = (1/resultC) * 100
print('{}%'.format(round(result, 2)))