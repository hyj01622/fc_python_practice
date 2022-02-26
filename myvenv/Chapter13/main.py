import os
import csv
from post import Post

# 파일 경로
file_path = './data.csv'

# post 객체를 저장할 리스트
post_list = []

# 에러 핸들링
class NotExist(Exception):
    def __init__(self):
        super().__init__('없는 글 번호 입니다')

class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__('음수나 0은 입력이 불가능합니다')


# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print('\n\n게시글 로딩중...')
    f = open(file_path, 'r', encoding='utf8')
    reader = csv.reader(f)

    for data in reader:
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2])
        post_list.append(post)
else:
    # 파일 생성하기
    f = open(file_path, 'w', encoding="utf8")
    f.close()



# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print('\n\n- 게시글 쓰기 -')
    title = input('제목을 입력해 주세요\n>>>')
    content = input('내용을 입력해 주세요\n>>>')

    # 글번호
    id = post_list[-1].get_id() + 1

    post = Post(id, title, content)
    post_list.append(post)
    print('=== 게시글이 등록되었습니다. ===')




# 게시글 목록
def get_posts():
    """게시글 목록 함수"""
    print('\n\n- 게시글 목록 -\n')
    for list in post_list:
        print(f'번호 : {list.get_id()}')
        print(f'제목 : {list.get_title()}')
        print(f'조회수 : {list.get_view_count()}\n')


    while True:
        try:
            choice = int(input('글 번호를 선택해 주세요(메뉴로 돌아가려면 -1을 입력)'))
            if choice > len(post_list):
                raise NotExist()
            elif choice == -1:
                break
            elif choice < 1:
                raise NegativeNumberError()
        except ValueError:
            print('숫자를 입력해 주세요')
        except NotExist as e:
            print(e)
        except NegativeNumberError as e:
            print(e)
        else:
            get_post_inner(choice)
            break



# 게시글 상세
def get_post_inner(id):
    post = post_list[id - 1]

    print(f'번호 : {post.get_id()}')
    print(f'제목 : {post.get_title()}')
    print(f'내용 : {post.get_content()}')
    print(f'조회수 : {post.get_view_count()}')



# 메뉴 출력하기
while True:
    print('\n- FASTCAMPUS BLOG -')
    print('- 메뉴를 선택해 주세요 -')
    print('1. 게시글 쓰기')
    print('2. 게시글 목록')
    print('3. 프로그램 종료')


    try:
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력해 주세요')
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            get_posts()
        elif choice == 3:
            print('=== 프로그램 종료 ===')
            break
