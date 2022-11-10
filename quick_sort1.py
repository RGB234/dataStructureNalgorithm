from typing import MutableSequence

def qsort(a:MutableSequence, left:int, right:int) -> None:
    pl =left
    pr = right
    x = a[(left + right)//2]

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

    if left < pr : qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

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
