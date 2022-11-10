
def kmp_match(txt:str, pat:str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1) #건너뛰기 표
    '''
    12번째 줄 마지막 경우에 pt == len(pat) -1 이 되고 while문 진행중에 pt == len(pat)이 됨
    만약 skip = [0] * len(pat)으로 정의하면 skip[pt] == pp에서 skip인덱스 범위를 초과
    '''

    #건너뛰기 표 만들기
    # skip[pt] = 0 이미 0이고, 여러모로 의도를 알 수 없어서 뺌
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] == pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    #문자열 검색
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]: #일치하는 구간을 찾았을때
            pt += 1
            pp += 1
        elif pp == 0: #처음부터 불일치 -> pt만 이동
            pt += 1
        else: #중간에 불일치가 나왔을때 -> pp를 skip 하여 다시검색
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트 입력: ')
    s2 = input('패턴 입력: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않음')
    else:
        print(f'{idx + 1} 번째 문자가 일치함')