from __future__ import annotations
from typing import Any, Type 

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None,
                right: Node = None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
    
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None: #검색실패
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
    
    def add(self, key: Any, value: Any) -> bool:

        def add_node(node: Node, key: Any, value: Any) -> None:
            if key == node.key:
                return False #이미 존재하는 키값
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root   #스캔중인 노드
        parent = None   #스캔중인 노드의 부모 노드
        is_left_child = True    #p는 parent의 왼쪽 자식 노드인지 여부

        '''제거할 노드 p 검색'''
        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True    #p는 parent의 왼쪽 자식 노드
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:          #삭제할 노드의 왼쪽자식노드가 없는 경우
            if p is self.root:      #삭제 노드가 루트인 경우
                self.root = p.right
            elif is_left_child:     #p가 parent의 왼쪽 자식이라면
                parent.left = p.right
            else:
                parent.right = p.right 
        elif p.right is None:       #오른쪽자식노드가 없는 경우
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:                       #자식 노드가 2개
            parent = p              #p를 부모로 하여 재검색
            left = p.left           #p의 왼쪽 자식
            is_left_child = True
            while left.right is not None:   #p의 왼쪽 서브트리 중 가장 큰 노드(left) 검색
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key    #삭제할 노드 p자리에 카피하여 옮기기
            p.value = left.value
            if is_left_child:           #빈 자리(옮겨지기 전) 메꾸기
                parent.left = left.left
            else:
                parent.right = left.left
        
        return True

    def dump(self, reverse = False) -> None:

        def print_subtree(node: Node):
            '''오름차순 출력'''
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node: Node):
            '''내림차순 출력'''
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)
        
        print_subtree_rev(self.root) if reverse  else print_subtree(self.root)

    def min_key(self) -> Any:
        '''가장 작은 키(key) 검색'''
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        '''가장 큰 키 검색'''
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key

