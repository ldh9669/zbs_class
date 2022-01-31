'''초보자를 위한 파이썬 300제
주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

지역코드	출생지
00 ~ 08	서울
09 ~ 12	부산
>> 주민등록번호: 821010-1635210
서울이 아닙니다.
>> 주민등록번호: 861010-1015210
서울 입니다.'''

seoul = ['00', '01', '02', '03', '04', '05', '06', '07', '08']
busan = ['09', '10', '11', '12']
resident_number = str(input('주민등록번호:'))
resident_number = resident_number[8:10]
if resident_number in seoul:
    print(input('서울 입니다.'))
elif resident_number in busan:
    print(input('부산 입니다.'))
else:
    print(input('알 수 없습니다'))