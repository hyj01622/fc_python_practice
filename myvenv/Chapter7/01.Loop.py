# 반복문
# : 반복해서 명령을 사용하고 싶을 때

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
# - 리스트 사용
champions = ['티모', '이즈리얼', '리신']

for champion in champions:
  print('선택한 챔피언은', champion, '입니다.')

# - 문자열 사용
message = '안녕하세요'

for word in message:
  print(word)

# - range 객체
# range(시작, 끝 + 1, 단계)
for i in range(0, 10, 2):
  print(i)