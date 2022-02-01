'''초보자를 위한 파이썬 300제
리스트를 아래와 같이 출력하라.

my_list = ["가", "나", "다", "라", "마"]
가 나 다
나 다 라
다 라 마'''

my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    print(my_list[i], my_list[i +1], my_list[i +2])