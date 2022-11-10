from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:

    i = 0 #패스 순서\
    ccnt = 0 #비교 횟수
    scnt = 0 #교환 횟수
    n = len(a)
    k = 0

    while k < n - 1:
        i += 1
        last = n - 1
        exchng = 0 #각 패스별 교환 횟수
        print(f'패스{ i }')
        for j in range(n-1, k, -1):
            for m in range(0, n-1):
                print(f'{a[m]:2}' + ('  ' if  m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j-1]
                last = j
                exchng += 1
        k = last

        for m in range(0, n-1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n-1]:2}')

        if exchng == 0: break

    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 했습니다')


if __name__ == '__main__':
    print("버블 정렬 수행")
    num = int(input('원소 수 입력: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    bubble_sort(x)

    print('오름차순 버블 정렬 완료')