
from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:

    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data #데이터
        self.next = next #리스트의 뒤쪽 포인터
        self.dnext = dnext #프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    
    def __init__(self, capacity: int):
        self.head = Null        #머리노드
        self.current = Null     #주목노드
        self.max = Null         #사용중인 꼬리 레코드
        self.deleted = Null     #프리 리스트(삭제한 레코드의 목록)의 머리노드
        self.capacity = Null    #리스트 크기
        self.n = [Node()] * self.capacity #리스트 본체
        self.no = 0             #리스트 노드 수

    def __len__(self) -> int:
        return self.no

    def gen_insert_index(self):
        '''다음에 삽입할 레코드의 인덱스'''
        if self.deleted == Null: #삭제 레코드가 존재하지 않는 경우
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max  #사용하지 않는 뒷쪽 레코드 사용
            else:
                return Null #리스트 크기 초과
        else:
            rec = self.deleted          #프리 리스트에서 맨 앞 rec꺼내기
            self.deleted = self.n[rec].dnext 
            return rec
    
    def delete_index(self, idx:int) -> None:
        '''레코드 idx를 프리 리스트에 등록'''
        if self.deleted == Null: #삭제 레코드가 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head #현재 스캔(주목)중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null #검색 실패

    def __contains__(self, data: Any) -> bool:
        '''연결 리스트에 data가 포함되어있는지 확인'''
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        '''머리 노드에 삽입'''
        ptr = self.head
        rec = self.gen_insert_index()
        if rec != Null:     #리스트 크기를 초과하지 않는다면
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        '''꼬리 노드에 삽입'''
        if self.head == Null: #리스트가 비어있을때
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next  #연결 리스트의 마지막
            rec = self.gen_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.n += 1

    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == Null: #노드가 1개뿐
                self.remove_first()
            else:
                ptr = self.head #스캔 중인 노드
                pre = self.head #스캔 중인 노드 앞쪽 노드

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                
                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p :int) -> None:
        '''레코드 p 삭제 (p는 삭제할 레코드의 커서)'''
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return  #p는 리스트에 존재하지 않음
                    # self.n[ptr].next = Null
                    self.delete_index(p)
                    self.n[ptr].next = self.n[p].next
                    self.current = ptr
                    self.no -= 1
    
    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head != Null:
            self.remove_first()
        self.current = Null

    def next(self) -> bool:
        '''주목 노드 한 칸 뒤로 이동'''
        if self.current == Null or self.n[self.current].next == Null:
            return False    #이동불가
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        '''주목 노드의 data 출력'''
        if self.current == Null:
            print('주목 노드가 없습니다')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        ptr = self.head
        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    
    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data