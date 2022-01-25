# #an = a1 + (n-1)d
# #sn = n(a1 + an) /2
# inputN1 = int(input('a1 입력'))
# inputD = int(input('공차 입력'))
# inputN = int(input('n 입력'))

# valueN = inputN1 + (inputN - 1) * inputD
# sumN = inputN * (inputN1 + valueN) / 2
# print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))


# sn = a1 * (1- r^n) / (1 - r)
inputN1 = int(input('a1 입력'))
inputR = int(input('공비 입력'))
inputN = int(input('n 입력'))

sumN = inputN1 * (1 - (inputR ** inputN)) / (1 - inputR)
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))