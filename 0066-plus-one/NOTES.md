```python3
ans = list(map(int, str(incrDigits)))
```

# map 함수 기본 문법
 

```python3
map(function, iterable)
```

* function: 각 요소에 적용할 함수입니다.
* iterable: 함수를 적용할 데이터 집합입니다.
 
map() 함수는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환합니다. 이때, function 함수는 각 요소를 인자로 받아서 처리하며, 함수의 반환값이 새로운 iterator의 각 요소가 됩니다.
