# 조건문
# : 조건에 따라 실행할 명령이 달라지는 것

origin_pass = '1234'
input_pass = input('패스워드를 입력하세요 >>>')

if origin_pass == input_pass : # 조건 A
  # 조건 A 참
  print('로그인 되었습니다.')
  print('반갑습니다.')
elif input_pass == '': # 조건 B
  # 조건 A 거짓, 조건 B 참
  print('아무것도 입력하지 않았습니다.')
else :
  # 조건 A, B 모두 거짓
  print('패스워드가 다릅니다.')
  print('패스워드를 확인하세요.')