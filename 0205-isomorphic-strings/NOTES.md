# zip func_ algoritm​
```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
```
### zip 함수 설명
파이썬의 내장 함수 zip()은 iterable, 즉 순회 가능한 객체를 인자로 받고 각 자료형의 각각의 요소를 나눈 후 인덱스끼리 잘라서 리스트로 반환해줍니다. - 여기서 말하는 iterable 자료형은 파이썬에서 리스트, 튜플 같은 반복 가능한 자료형을 의미합니다.

 

위 코드에서는 s와 t를 set()함수로 집합화 시킨 후, 그 길이가 같은지를 판별했고, 추가로, zip()함수로 (s,t) 쌍을 집합화해서 그것들의 길이도 비교했습니다.

위에서 살펴봤던 예시를 비교해보자면, aaabbbba 와 aaabbbab 에서

set(s) => {a,b} 이므로 len(set(s)) 는 2가 되겠고, len(set(t)) 도 마찬가지로 2가 됩니다.

하지만, set(zip(s,t))는 {(a,a), (b,b), (b,a), (a,b)}가 되고 이것들의 길이는 4가 되므로 false를 리턴하게 됩니다. zip함수로 동형사상까지 검사하는 효율높은 코드라고 할 수 있겠죠!?
