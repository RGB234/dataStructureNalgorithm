'''원형 이중 연결 리스트'''

from __future__ import annotations
from typing import Any, TypedDict

class Node:

    def __init__(self, data: Any = None, prev: Node = None,
                next: Node = None) -> None:

        self.data = data
        self.prev = prev or self #앞쪽 포인터, prev가 None으로 전달받을 경우 self로 대입
        self.next = next or self #뒤쪽 포인터

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = self.current = Node()   #더미 노드 생성
        self.no = 0                         #연결리스트 노드 수

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        cnt = 0
        ptr = self.head.next #현재 스캔중인 노드, self.head는 더미이므로 self.head.next 부터 시작
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        '''
        dunder(underscore * 2) 를 사용하여 클래스의 인스턴스에 in을 적용가능
        즉, self.__contains__(x)를 x in obj로 작성가능
        '''
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        if self.is_empty():
            print('주목 노드는 없습니다 (연결리스트가 비어있음)')
        else:
            print(self.current.data)

    def print(self) -> None:
        '''모든 노드의 데이터 출력'''
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        '''모든 노드의 데이터 역순출력'''
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        '''주목 노드 한 칸 뒤로 이동'''
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        '''주목 노드 한 칸 앞으로 이동'''
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        '''주목 노드 바로 뒤에 노드 삽입'''
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        self.current = self.head
        self.add(data)

    def add_last(self, data: Any) -> None:
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next
        
    def remove(self, p: Node) -> None:
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0

    def __iter__(self) -> DoubleLinkedListIterator:
        '''이터레이터반환'''
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        '''내림차순 이터레이터 반환'''
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data