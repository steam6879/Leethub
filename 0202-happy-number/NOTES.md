```python3
def isHappy(self, n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True
```
`n = sum([int(i) ** 2 for i in str(n)])`
sum함수를 이용하여 간결한 코드를 작성할 수 있다.
