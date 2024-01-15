# Dictionary/Hash table
```python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = {}
        while head:
            if head in m:
                return True
            else:
                m[head] = True

            head = head.next
        
        return False
```
내가 생각한 방법.
* `if head is None`은 잘못 된 표현이다. `if head`가 올바른 표현이다.​ 이것으로 처음에 컴파일 에러가 나와서 고생했다.

# Two pointers
```python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if  not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next
        
        return True
```
>탐색을 하는 와중 fast 포인터가 가리키는 노드가 없거나 혹은 fast 포인터가 가리키는 노드 다음 노드가 없다면 false를 리턴해주고 종료한다.
>
>이 경우 fast 포인터가 주어진 전제 linked list를 탐색했는데도 불구하고 그 와중에 slow 포인터가 만나지 못했다는 뜻이기 때문에 cycle이 존재하지 않음을 의미한다.
>
>만약 이 경우가 아니라면 slow 포인터는 오른쪽으로 한 칸, fast 포인터는 오른쪽으로 투 칸씩 움직이면서 탐색을 계속한다.
>
>While loop는 slow 포인터와 fast 포인터가 만나지 않는 이상 계속 돌게된다.
