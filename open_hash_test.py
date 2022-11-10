# 오픈 주소법을 적용한 해시 클래스 OpenHash 테스트

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13) #크기가 13인 해시테이블로 지정

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력: '))
        val = input('추가할 값을 입력: ')
        if not hash.add(key, val):
            print('이미 존재하는 키값입니다')
    
    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력: '))
        if not hash.remove(key):
            print('존재하지 않는 키값입니디')

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력: '))
        t = hash.search(key)
        if t is not None:
            print(f'{key} : {t}')
        else:
            print('해당 키값은 존재하지 않습니다')

    elif menu == Menu.덤프:
        hash.dump()
        
    else:
        break