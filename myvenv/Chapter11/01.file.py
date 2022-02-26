# 순서
# 파일 열기 / 파일 쓰기 / 파일 닫기

file = open('./data.txt', 'w', encoding='utf8')
file.write('hello')
file.close()

file = open('./data.txt', 'a', encoding='utf8')
file.write('\nworld')
file.close()

file = open('./data.txt', 'r', encoding='utf8')

data = file.read()

print(data)

file.close()

# 파일 한줄 읽기
# while True:
#     data = file.readline()
#     print(data, end="")
#
#     if data == '':
#         break

# file.close()