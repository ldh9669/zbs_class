'''초보자를 위한 파이썬 300제
주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

>> 주민등록번호: 821010-1635210
남자'''

resident_number = str(input('주민등록번호:'))
resident_number = resident_number[7]
if resident_number in ['1', '3']:
    print('남자')
elif resident_number in ['2', '4']:
    print('여자')
else:
    print('알수없음')