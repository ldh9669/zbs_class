'''초보자를 위한 파이썬 300제
191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.

2000.28
3050.427
2050.2870000000003
1980.2772
----
7501.05
2050.2870000000003
2050.2870000000003
1980.2772
----
15452.163
15052.107
15552.177
14902.086000000001
----'''

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]]
for a in data:
    for b in a:
        print(b *1.00014)
    print('----')