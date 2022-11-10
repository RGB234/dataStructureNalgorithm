#오픈 주소법

from __future__ import annotations
from typing  import Any, Type
from enum import Enum
import hashlib

#버킷의 속성
class Status(Enum):
    OCCUPIED = 0 #데이터 저장됨
    EMPTY = 1 #데이터 비어있음
    DELETED = 2 #데이터 삭제됨

class Bucket:
    '''해시를 구성하는 버킷'''

    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        '''초기화'''
        self.key = key
        self.value = value
        self.stat = stat
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        '''모든 필드에 값을 설정'''
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat

class OpenHash:
    '''오픈주소법 활용 해시 클래스'''

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int): #key 가 int형인경우
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) %self.capacity)

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key: #찾음
                return p
            hash = self.rehash_value(key)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        '''키가 key인 원소를 검색하여 value 반환'''
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False #이미 존재하는 key

        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False #해시 테이블이 가득 참

    def remove(self, key: Any) -> bool:
        p = self.search_node(key)
        if p is None:
            return False #존재하지 않는 key
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        '''해시 테이블을 덤프(모두 꺼내 보여줌)'''
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제됨--')
