class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        newTail = head.next
        newHead = self.reverseList(head.next)

        newTail.next = head
        head.next = None

        return newHead