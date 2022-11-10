from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    
    def __init__(self) -> None:
        self.no = 0             #노드 개수
        self.head = None        #머리 노드
        self.current = None     #주목 노드

    def __len__(self) -> int:
        
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0 #몇 번째(첫번째는 cnt=0) 노드를 주목하고있는지
        ptr = self.head #주목하는 노드
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        '''연결 리스트에 data가 포함되어있는지 확인'''
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        ptr = self.head #삽입 전 머리노드
        self.head = self.currnet = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self) -> None:
        if self.head is not None: #노드가 1개 이상
            if self.head.next is None: #노드가 1개
                self.remove_first()
            else:
                ptr = self.head #스캔중인 노드
                pre = self.head #스캔중인 노드의 앞쪽 노드 
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
    
    def remove(self, p:Node) -> None:
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return #ptr은 리스트에 존재하지 않음
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None: #리스트가 빌 때 까지
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self) -> bool:
        '''주목노드 한 칸 뒤로 이동'''
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True
    
    def print_current_node(self) -> None:
        if self.current is None:
            print('주목 노드가 존재하지 않음')
        else:
            print(self.current.data)
    
    def print(self) -> None:
        
        ptr = self.head

        if ptr is None:
            print('노드가 모두 비어있음')
        else:
            while ptr is not None:
                print(ptr.data)
                ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        '''이터레이터를 반환'''
        return LinkedListIterator(self.head)

class LinkedListIterator:

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

     