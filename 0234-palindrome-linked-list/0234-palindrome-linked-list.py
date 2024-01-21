# Definition for singly-linked list.
from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        que = deque()
        while head:
            que.append(head.val)
            head = head.next

        while len(que) > 1:
            if que.popleft() != que.pop():
                return False
        else:
            return True