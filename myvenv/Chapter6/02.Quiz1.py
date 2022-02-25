# result = [33, 40, 12, 63, 52]
result = [33, 40, 12, 63, 52]

# 출력 1: 9를 리스트 마지막에 추가하기
result.append(9)

print(result)

# 출력 2 : 2번째 아이템을 50으로 변경

result[1] = 50

print(result)

# 출력 3 : 3번째 아이템부터 6번째 데이터를 슬라이싱

sliced = result[2:]

print(sliced)

# 출력 4 : 오름차순으로 정렬

result.sort()

print(result)