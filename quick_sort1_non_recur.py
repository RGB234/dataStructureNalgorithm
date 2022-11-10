from fixed_stack import FixedStack
from typing import MutableSequence

def qsort(a:MutableSequence, left:int, right:int) -> None:
    '''비재귀적 퀵정렬'''
    
    range = FixedStack(right - left + 1) #나눌 범위에서 맨 앞 원소의 인덱스와 맨 끝 원소 인덱스를 조합한 튜플스택
    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left + right) // 2]

        print(f'a[{left}] ~ a[{right}] :', *a[left : right +1])

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr : range.push((left,pr))
        if pl < right: range.push((pl,right))

def qucik_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) -1)

if __name__ == '__main__':
    print('퀵 정렬 수행')
    num = int(input('원소 수 입력: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    qucik_sort(x)

    print('오름차순 정렬 완료') 
    for i in range(num):
        print(f'x[{i}] = {x[i]}')           
