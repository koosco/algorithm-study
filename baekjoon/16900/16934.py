import sys

read = sys.stdin.readline


class Node:
    def __init__(self):
        self.cnt = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()
        self.res = []

    def insert(self, name: str):
        node = self.head
        find_new_node = False
        for i in range(len(name)):
            if name[i] not in node.children:
                node.children[name[i]] = Node()
                if not find_new_node:
                    self.res.append(name[:i+1])
                find_new_node = True
            node = node.children[name[i]]
        node.cnt += 1
        if not find_new_node:
            self.res.append(name + str(node.cnt) if node.cnt > 1 else name)

    def get_res(self):
        return self.res


names = [read().rstrip() for _ in range(int(read()))]
trie = Trie()
for name in names:
    trie.insert(name)
print(*trie.get_res(), sep='\n')
