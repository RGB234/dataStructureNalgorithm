from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    '''도수 정렬(원소값은 0이상 max이하의 정수)'''
    n = len(a)
    f = [0] * (max + 1) #누적 도수 분포표 (0 ~ max max+1개 )
    b = [0] * n

    for i in range(n): f[a[i]] += 1
    for i in range(1, max + 1): f[i] += f[i-1]
    for i in range(n-1, -1, -1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n): a[i] = b[i]

def couting_sort(a: MutableSequence) -> None:
    fsort(a, max(a))

if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        while True: #양수만 입력받도록 제한
            x[i] = int(input(f'x[{i}] :'))
            if x[i] >= 0: break

    couting_sort(x)

    print('오름차순 정렬 완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')