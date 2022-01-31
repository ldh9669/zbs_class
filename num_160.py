'''초보자를 위한 파이썬 300제
파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
intra.c
define.h'''

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i[-1] == 'h' or i[-1] == 'c':
        print(i)