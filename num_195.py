'''초보자를 위한 파이썬 300제
ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
화면에 종가데이터를 출력하라.

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
100
190
310'''

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

result = []
for list in ohlc:
    for value in list:
        result.append(value)
for a in result[7::4]:
    print(a)