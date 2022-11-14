
from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '오름차순으로덤프', '내림차순으로덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()

while True:
    menu = select_Menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키를 입력: '))
        val = input('삽입할 값을 입력: ')
        if not tree.add(key, val):
            print('삽입 실패(중복된 키값)')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력: '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키에 해당하는 값은 {t}')
        else:
            print('해당 키 값이 존재하지 않습니다')

    elif menu == Menu.오름차순으로덤프:
        print('빈 트리입니다') if tree.root is None else tree.dump()

    elif menu == Menu.내림차순으로덤프:
        print('빈 트리입니다') if tree.root is None else tree.dump(reverse = True)

    elif menu == Menu.키의범위:
        print(f'{tree.min_key()} ~  {tree.max_key()}')

    else:
        break