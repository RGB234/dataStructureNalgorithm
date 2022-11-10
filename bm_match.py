
def bm_match(txt: str, pat:str) -> int:
    '''보이어-무어법'''
    skip = [None] * 256

    #건너뛰기 표
    for pt in range(256):
        skip[pt] = len(pat) #건너뛰기 표 초기화
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1
    #skip[ord(pat[len(pat)-1])] = len(pat) - (len(pat) - 1) - 1 = 0, 실제로 확인결과 맞음
    
    #검색하기
    # print(pt) -> 3
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp\
            else len(pat) - pp
            # 1 <= len(pat) - pp <= len(pat), 0 < skip[ord(txt[pt])] <= len(pat)
    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력: ')
    s2 = input('검색할 패턴을 입력: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('검색한 패턴이 텍스트안에 존재하지 않음')
    else:
        print(f'{idx + 1}번째 문자가 일치')