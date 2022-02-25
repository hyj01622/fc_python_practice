# while
i = 0

while i < 10:
  print(i, '번째 다짐')
  i += 2


while True:
  x = input('종료하려면 exit을 누르세요 >>>')
  if x == 'exit':
    break