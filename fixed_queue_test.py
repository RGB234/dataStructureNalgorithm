from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64) #크기는 64

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}') #self.__len__()
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 데이터 입력: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다')
                        
    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'디큐한 데이터는 {x}')
        except FixedQueue.Empty:
            print('큐가 비어있습니다')

    elif menu == Menu.피크:
        try:
            print(f'피크한 데이터 : {q.peek()}')
        except FixedQueue.Empty:
            print('큐가 비어있습니다')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력: '))
        if x in q:
            print(f'{q.count(x)}개가 검색됨. 맨 앞의 인덱스 번호는 {q.find(x)}')
        else:
            print('검색한 값이 큐에 존재하지 않습니다')

    elif menu == Menu.덤프:
        q.dump()

    else:
        break
