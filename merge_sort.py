from typing import MutableSequence

def merge_sort(a:MutableSequence) -> None:
    '''병합정렬'''

    def _merge_sort(a: MutableSequence, left:int, right:int) -> None:
        '''a[left] ~ a[right] 병합정렬(재귀)'''
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)
            
            p = j = 0
            i = k = left
            '''buff에 분할된 배열 병합'''
            while i <= center: #절반 중 왼쪽 buff[0]~ buff[center - left]에 복사
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i <= right and j < p: #절반 중 오른쪽, p = center - left + 1개(buff에 복사된 a의 앞쪽배열 원소수)
                # 뒷쪽배열을 다 복사할때까지 or 앞쪽배열을 다 복사(병합)할때까지
                if buff[j] <= a[i]:
                    a[k] = buff[j] #더 작은 값을 a에 복사
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while i <= right: #a[i]에 남은 원소 복사
                a[k] = a[i]
                k += 1
                i += 1

            while j < p: #buff[j]에 남은 원소 복사
                a[k] = buff[j]
                k += 1
                j += 1

    
    n = len(a)
    buff = [None] * n #작업용 배열
    _merge_sort(a, 0, n-1)
    del buff

if __name__ == '__main__':
    print('병합 정렬 수행')
    num = int(input("원소 수 입력: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    merge_sort(x)

    print('오름차순으로 정렬 완료')
    for i in range(num):
        print(f'x[{i}] : {x[i]}')