'''초보자를 위한 파이썬 300제
my_list를 아래와 같이 출력하라.

my_list = ["가", "나", "다", "라"]
가 나
나 다
다 라'''

my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i], my_list[i +1])