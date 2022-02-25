# 부모클래스
import random


class Monster:
  # 클래스 변수 // 인스턴스 모두가 공유하는 변수
  max_num = 1000

  # __init__은 인스턴스가 생성될 때 실행되는 함수
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
    Monster.max_num -= 1

  def move(self):
    print(f'[{self.name}] : 지상에서 이동하기')

# 자식클래스
class Wolf(Monster):
  pass

class Shark(Monster):
  def move(self): # 메서드 오버라이딩
    print(f"[{self.name}] : 헤엄치기")

class Dragon(Monster):
  # 생성자 오버라이딩
  def __init__(self, name, health, attack):
    super().__init__(name, health, attack)
    self.skills = ('불 뿜기', '꼬리치기', '날개치기')

  def move(self):
    print(f"[{self.name}] : 날기")

  def skill(self):
    print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")


wolf = Wolf('울프', 800, 90)
print(wolf.max_num)
wolf.move()

shark = Shark('샤크', 1200, 120)
print(shark.max_num)
shark.move()

dragon = Dragon('드래곤', 4000, 300)
dragon.skill()

  # def say(self): # 몬스터다!
  #   print('나는 몬스터다')

  # def decrease_health(self, num): # 체력 감소
  #   self.health -= num

  # def increase_health(self, num): # 체력 증가
  #   self.health += num

# goblin = Monster(800, 120, 300) # 이 때 __init__이 실행됨

# goblin.decrease_health(300)

# print(goblin.health)