# iterative algorithm
```python3
class Solution(object):
    def isSymmetric(self, root):
        queue = [root, root]
        while len(queue) != 0:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            else:
                if left.val == right.val:
                    queue.extend([left.left, right.right, left.right, right.left])
                else:
                    return False
        return True​
```

## 풀이
이 문제를 푸는 방법은 재귀(recursively)와 반복(iteratively) 2가지 방법이 있다.

우선 재귀로 푸는 방법을 살펴보자. 보통 Tree 문제를 재귀로 풀때에는 root를 확인하고, 왼쪽 서브트리와 오른쪽 서브트리를 확인하는 방식으로 구현한다. 이 문제도 똑같은 방법으로 해결 가능하다. 단, 주의할 점은 대칭임을 확인하기 위해서는 왼쪽 서브트리와 오른쪽 서브트리를 반대로 비교해야 한다. 즉 두 서브트리의 root가 같은지 확인하고, 왼쪽 서브트리의 left가 오른쪽 서브트리의 right가 같은지, 왼쪽 서브트리의 right이 오른쪽 서브트리의 leftt가 같은지 확인하면 된다.

같은 풀이를 iterative하게도 풀 수 있다. 재귀로 풀었던 것을 큐(Queue)를 이용하여 root부터 더 이상 자식이 없는 leaf까지 순회하면 된다.

# DFS(stack) algorithm
```python3
class Solution:
    def isSymmetric(self, root):
        stack = []
        if root: stack.append([root.left, root.right])

        while(len(stack) > 0):
            left, right = stack.pop()
            
            if left and right:
                if left.val != right.val: return False
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])
        
            elif left or right: return False
        
        return True
```
