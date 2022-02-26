class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__('양수는 입력 불가')

# raise 구문 사용해서 강제로 에러 발생

try:
    number = int(input('음수를 입력해 주세요 >>>'))
    if number >= 0:
        raise PositiveNumberError()
except PositiveNumberError as e:
    print('에러발생!', e)