import sys
from collections import defaultdict
from typing import Dict, Tuple
read = sys.stdin.readline


class Traversal:
    def preorder(self, node: str='A'):
        if node == '.':
            return
        print(node, end='')
        self.preorder(tree[node][0])
        self.preorder(tree[node][1])

    def inorder(self, node: str='A'):
        if node == '.':
            return
        self.inorder(tree[node][0])
        print(node, end='')
        self.inorder(tree[node][1])

    def postorder(self, node: str='A'):
        if node == '.':
            return
        self.postorder(tree[node][0])
        self.postorder(tree[node][1])
        print(node, end='')


tree: Dict[str, Tuple[str, str]] = defaultdict()
n: int = int(read())
for _ in range(n):
    root: str
    left: str
    right: str

    root, left, right = read().split()
    tree[root] = (left, right)

sol = Traversal()
sol.preorder()
print()
sol.inorder()
print()
sol.postorder()