'''초보자를 위한 파이썬 300제
리스트에 저장된 데이터를 아래와 같이 출력하라.

apart = [ [101, 102], [201, 202], [301, 302] ]
302 호
301 호
202 호
201 호
102 호
101 호'''

apart = [ [101, 102], [201, 202], [301, 302] ]
for floor in apart[::-1]:
    for unit in floor[::-1]:
        print(unit, '호')