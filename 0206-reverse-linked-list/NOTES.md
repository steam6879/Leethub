# ​iteratively algorithm
```python3
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        node = head
        while curr:
            tempNext = curr
            curr.next = prev
            prev, curr = curr, tempNext.next
        
        return prev
```

# stack algorithm
```python3
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        node = head

        while node:
            stack.append(node)
            node = node.next
        
        dummy = ListNode(-1)
        node = dummy

        while stack:
            node.next = stack.pop
            node = node.next
        
        node.next = None

        return dummy.next
```

[youtube] https://www.youtube.com/watch?v=O4po8XPf5Hc&t=2s
