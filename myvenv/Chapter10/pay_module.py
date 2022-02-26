# 결제 정보, 관리 모듈
# 변수
version = 2.0

# 함수
def print_author():
    print('스타트코딩')

# 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"

    # 해당 파일을 직접 실행 했을 때만 실행됨
    if __name__ == '__main__':
        print('pay 모듈 실행')