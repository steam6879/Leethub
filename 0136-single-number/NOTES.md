# Using xor 연산
```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            answer ^= n
        return answer
```
xor연산을 사용했다.
xor연산의 특징은 다음과 같다.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
,
a ^ 0 = a

또한, xor은 교환법칙이 가능하다.
즉, a ^ b = b ^ a 이다.

위 두 특징을 이용하여, nums list의 모든 element를 누적해서 xor연산을 거치면,
마지막 남은 수가 한번만 존재하는 수이다.

[4, 2, 1, 2, 1]
에서 교환법칙을 통해 정리하면

0 ^ 4 ^ 2 ^ 1 ^ 2 ^ 1 = 0 ^ 4 ^ 1 ^ 1 ^ 2 ^ 2
= 4​
