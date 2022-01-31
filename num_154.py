'''초보자를 위한 파이썬 300제
리스트에서 세 글자 이상의 문자를 화면에 출력하라

리스트 = ["I", "study", "python", "language", "!"]
study
python
language'''

리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)