
from typing import Any

class FixedStack:
    '''고정 길이 스택 클래스'''

    class Empty(Exception):
        '''비어있는 FixedStack 에 pop 또는 peak 할 때 내보내는 예외처리'''
        pass
    
    class Full(Exception):
        '''가득한 FixedStack에 push 할 때 내보내는 예외처리'''
        pass

    def __init__(self, capacity: int =256 ) -> None:  #capacity 기본값은 256, 지정안할시 256이 된다
        self.stk = [None] * capacity #스택 본체
        self.capacity = capacity #스택 크기
        self.ptr = 0 #스택 포인터 

    def __len__(self) -> int: 
        #dunder(underscore * 2) 를 사용하여 class의 인스턴스를 len()함수에 적용가능
        #즉 , obj.__len__ 을 len(obj)로 작성가능
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0 #프로그램 오류로 0보다 작아지는 경우도 고려하여 이를 방지

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        '''가장 꼭대기에 있는 데이터 들여다보기(pop하지는 않음)'''
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        '''스택에 value를 찾아 인덱스 반환(top에서부터 선형 검색)'''
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        '''스택에 있는 value 의 개수 반환'''
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool: 
        '''스택에 value가 있는지 판단'''
        #dunder(underscore * 2) 를 사용하여 클래스의 인스턴스에 in을 적용가능
        #즉, obj.__contains__(x)를 x in obj로 작성가능
        return self.count(value) > 0

    def dump(self) -> None:
        '''bottom 부터 top 순으로 출력'''
        if self.is_empty():
            print('비어있는 스택입니다')
        else:
            print(self.stk[:self.ptr])