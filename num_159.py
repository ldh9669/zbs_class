'''초보자를 위한 파이썬 300제
파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
define.h'''

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i[-2:] == ".h":
        print(i)