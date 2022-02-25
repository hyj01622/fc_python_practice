# 클래스 실습
# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 : 착용효과, 착용하기
# 소모품 : 사용효과, 사용하기
# 단 버리기는 버릴 수 있는 아이템만 가능

# Item
# 이름 // name : str
# 가격 // price : int
# 무게 // weight : float
# 버리기가능 // isdropable: bool
# 판매하기 // sales(): None
# 버리기 // discard(): None

# WearableItem
# 상속//
# 효과 // effect : str
# 착용하기 // wear() : None

# UseableItem
# 상속//
# 효과 // effect : str
# 사용하기 // use() : None

class Item:
  def __init__(self, name, price, weight, isdropable):
    self.name = name
    self.price = price
    self.weight = weight
    self.isdropable = isdropable

  def sale(self):
    print(f"[{self.name}] 판매가격은 [{self.price}]")

  def discard(self):
    if self.isdropable:
      print(f"[{self.name}] 아이템을 버렸습니다.")
    else:
      print(f"[{self.name}] 아이템을 버릴 수 없습니다.")



class WearableItem(Item):
  def __init__(self, name, price, weight, isdropable):
    super().__init__(name,price,weight,isdropable)
    self.effect = '착용효과'

  def wear(self):
    print(f"[{self.name}] 아이템을 착용했습니다. [{self.effect}]")



class UseableItem(Item):
  def __init__(self, name, price, weight, isdropable):
    super().__init__(name,price,weight,isdropable)
    self.effect = '사용효과'

  def use(self):
    print(f"[{self.name}] 아이템을 사용했습니다.")



sword = WearableItem('검', 4000, '3kg', False)

print(sword.discard())
