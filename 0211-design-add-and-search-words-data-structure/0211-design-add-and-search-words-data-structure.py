class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.head = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.head

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.data = word

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.data is not None

            char = word[i]
            if char in node.children:
                return dfs(node.children[char], i + 1)
            if char == ".":
                return any(dfs(node.children[k], i + 1) for k in node.children)

            return False

        return dfs(self.head, 0)
