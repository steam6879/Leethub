# XOR algorithm
풀이 방법
easy 문제라 쉽게 풀어 제출했지만, discuss에서 비트 연산과 ASCII 코드를 이용한 풀이 방법이 있어 포스팅하게 되었다. 

아래 Example1과 같이 추가된 문자 1개만 반환하면 되는 문제다. 


[Example 1]

Input: s = "abcd", t = "abcde"

Output: "e"

Explanation: 'e' is the letter that was added.

 

 

이 문제에서는 XOR 연산을 사용하려고 하는데, 먼저 XOR 연산을 간단히 정의해보면

"같으면 0, 다르면 1을 반환"하는 연산이다. 

그럼 아래의 식이 성립한다는 것을 알 수 있다.

 

 

**0^ord('a') == ord('a')
0과 ord('a')의 연산은 ord('a')와 같다.**

**ord('a')^ord('a')^ord('b') == ord('b')
a는 같으므로 0, 0^ord('b')이므로 ord('b')와 같다.**
 

(파이썬의 ord()가 ASCII 코드값을 반환해준다)

따라서 input string 두 개를 합쳐서 XOR 연산을 해주면 최종적으로 1개 문자의 ASCII 코드값이 남게 된다.

이를 다시 chr()함수로 ASCII -> 문자로 변경해준다.

```python3
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = 0
        for c in s+t:
            x ^= ord(c)
            
        return chr(x)​
```
