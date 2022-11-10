from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    '''메뉴 선택'''
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)
         
hash = ChainedHash(13) #해시테이블 크기는 13으로 지정

while True:
        menu = select_menu()
         
        if menu == Menu.추가:
            key = int(input('추가할 키를 입력: '))
            val = input('추가할 값을 입력: ')
            if not hash.add(key, val):
                print('추가 실패(이미 존재하는 key입니다)')

        elif menu == Menu.삭제:
            key = int(input('삭제할 키를 입력: '))
            if not hash.remove(key):
                print('삭제 실패(존재하지 않는 key입니다)')

        elif menu == Menu.검색:
            key = int(input('검색할 키를 입력: '))
            t = hash.search(key)
            if t is not None:
                 print(f' {key} : {t}(value) ')
            else:
                print('검색 실패(존재하지 않는 key입니다)')
            
        elif menu == Menu.덤프:
            hash.dump()
            
        else:
            break