# stack algoritm
```python3
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        if stack[::] == stack[::-1]:
            return True
        else:
            return False
```
slicing을 이용하여 palindrome을 판단하였다.
