import random

lottery = []

def getRandomNumber():
  number = random.randint(1, 45)
  return number

count = 0

while True:
  if count > 5:
    break
  randomNum = getRandomNumber()
  lottery.append(randomNum)
  count += 1

lottery.sort()

print(lottery)