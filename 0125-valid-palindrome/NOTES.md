# ​Solution
## 1) 리스트로 변환
```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
				# 영문자, 숫자만 추출하여 리스트에 한 개의 문자/숫자씩 요소로 추가하는 전처리 과정
        strs = []
        for char in s: # 문자열의 문자를 iteration
            if char.isalnum(): # 문자가 영문자, 숫자이면
                strs.append(char.lower()) # 소문자로 변경하여 리스트에 추가
        
				# 팰린드롬 판별 여부 판별
        while len(strs) > 1: # 리스트의 요소가 2개 이상일 때
            if strs.pop(0) != strs.pop(): # 맨 앞 문자/숫자와 맨 뒤 문자/숫자가 같지 않으면
                return False
        
        return True
```
* isalnum() : 영문자, 숫자 여부를 판별하는 함수
* pop(index) : pop(0) 이면 리스트의 맨 앞의 값을 가져온다. pop() 이면 맨 뒤의 값을 가져온다.

## 2) 데크 자료형을 이용한 최적화
리스트만으로 풀 수 있지만, 데크(Deque)를 명시적으로 선언하면 속도를 좀 더 높일 수 있다.

리스트의 pop(0) 이 O(n)인 데 반해, 데크의 popleft()는 O(1)이기 때문이다. 각각 n번 반복하면, 리스트 구현은 O(n^2), 데크 구현은 O(n)으로 성능 차이가 크다.

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
				# 자료형 데크로 선언
        strs: Deque = collections.deque() 
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
```

## 3) 슬라이싱 사용
알고리즘이라 부를 만한 게 없이 정규식으로 불필요한 문자를 필터링하고, 문자열을 조작할 수 있는 슬라이싱(Slicing)을 사용한다. 1) 풀이의 isalnum() 은 모든 문자를 일일이 점검했지만 여기서는 문자열 전체를 한 번에 영숫자만 걸러내도록 정규식으로 처리

슬라이싱은 코드가 훨씬 줄어듦은 물론, 내부적으로 C로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다.

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
				# 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 슬라이싱
```
파이썬 문자열 슬라이싱은 위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며 이를 통해 연결된 객체를 찾아 실제 값을 찾아내는데, 이 과정은 매우 빠르게 진행되므로 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.
