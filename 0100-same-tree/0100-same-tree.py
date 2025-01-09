class Solution:       # BFS gpt 01 ver`
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        que = deque([(p, q)])

        while que:
            node1, node2 = que.popleft()

            # If both nodes are present and match
            if node1 and node2 and node1.val == node2.val:
                que.append((node1.left, node2.left))
                que.append((node1.right, node2.right))
            # If one node is missing or values mismatch
            elif node1 or node2:
                return False

        # All compared nodes matched
        return True
