from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    
    def __init__(self, key:Any, value:Any, next:Node) -> None:
        '''초기화'''
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    
    def __init__(self, capacity:int) -> None:
        '''초기화'''
        self.capacity = capacity #해시 테이블 크기 지정
        self.table = [None] * self.capacity #해시 테이블 선언
        
    def hash_value(self, key:Any) -> int:
        '''해시값을 구함'''
        if isinstance(key, int): #key 가 int형인 경우
            return key % self.capacity
        #key 가 문자형인 경우 문자열의 해쉬값을 구함
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key:Any) -> Any:
        '''키가 key 인 원소를 검색하여 값을 반횐'''
        hash = self.hash_value(key) #검색하는 키의 해쉬값
        p = self.table[hash] #노드를 주목
        
        while p is not None:
            if p.key == key:
                return p.value #검색성공
            p = p.next #다음 노드 주목
        
        return None
    
    def add(self, key:Any, value:Any) -> bool:
        '''키가 key, 값이 value인 원소를 추가'''
        hash = self.hash_value(key) # 추가하는 key 의 해쉬값
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False #추가 실패 (이미 존재)
            p = p.next # 뒤쪽 노드 주목
        
        temp = Node(key, value, self.table[hash]) #연결리스트 맨 앞에 노드 추가
        self.table[hash] = temp #해쉬 테이블이 추가된 노드(temp) 를 연결하도록 self.table[hash] 갱신
        return True
    
    def remove(self, key:Any) -> boll:
        '''키가 key인 원소 삭제'''
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None #바로 앞의 노드
         
        while p is not None:
            if p.key == key: #검색 성공시
                if pp is None:
                    self.table[hash] = p.next #검색된 p 가 연결리스트중 가장 앞에 있을 경우
                else:
                    pp.next = p.next
                return True #삭제 성공
                pp = p
                p = p.next
            return False #삭제 실패 (key 가 존재하지 않음)
        
    def dump(self) -> None:
        '''해쉬 테이블을 덤프(해시 테이블 통째로 출력)'''
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next
            print()