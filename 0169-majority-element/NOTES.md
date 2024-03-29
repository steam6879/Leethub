# Approach 1: Sorting
## Intuition:
The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

## Explanation:
* The code begins by sorting the array nums in non-decreasing order using the sort function from the C++ Standard Library. This rearranges the elements such that identical elements are grouped together.
* Once the array is sorted, the majority element will always be present at index n/2, where n is the size of the array.
* This is because the majority element occurs more than n/2 times, and when the array is sorted, it will occupy the middle position.
* The code returns the element at index n/2 as the majority element.
The time complexity of this approach is O(n log n) since sorting an array of size n takes O(n log n) time.

## Code
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
```

# Approach 3: Moore Voting Algorithm
## Intuition:
The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, it will always remain in the lead, even after encountering other elements.

## Explanation:
Algorithm:

Initialize two variables: count and candidate. Set count to 0 and candidate to an arbitrary value.
Iterate through the array nums:
a. If count is 0, assign the current element as the new candidate and increment count by 1.
b. If the current element is the same as the candidate, increment count by 1.
c. If the current element is different from the candidate, decrement count by 1.
After the iteration, the candidate variable will hold the majority element.
## Explanation:

1. The algorithm starts by assuming the first element as the majority candidate and sets the count to 1.
2. As it iterates through the array, it compares each element with the candidate:
3. a. If the current element matches the candidate, it suggests that it reinforces the majority element because it appears again. Therefore, the count is incremented by 1.
4. b. If the current element is different from the candidate, it suggests that there might be an equal number of occurrences of the majority element and other elements. Therefore, the count is decremented by 1.

Note that decrementing the count doesn't change the fact that the majority element occurs more than n/2 times.
If the count becomes 0, it means that the current candidate is no longer a potential majority element. In this case, a new candidate is chosen from the remaining elements.
The algorithm continues this process until it has traversed the entire array.
The final value of the candidate variable will hold the majority element.
## Explanation of Correctness:
The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array. This assumption guarantees that even if the count is reset to 0 by other elements, the majority element will eventually regain the lead.

Let's consider two cases:

1. If the majority element has more than n/2 occurrences:
  * The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

2. If the majority element has exactly n/2 occurrences:
  * In this case, there will be an equal number of occurrences for the majority element and the remaining elements combined.
However, the majority element will still be selected as the final candidate because it will always have a lead over any other element.
In both cases, the algorithm will correctly identify the majority element.

The time complexity of the Moore's Voting Algorithm is O(n) since it traverses the array once.

This approach is efficient compared to sorting as it requires only a single pass through the array and does not change the original order of the elements.

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:

                count -= 1
        
        return candidate
```

# Boyer-Moore 과반수 투표 알고리즘
Boyer-Moore 과반수 투표 알고리즘(majority vote algorithm)[1]은 배열에 포함된 원소들 중 절반 이상 포함된 원소를 linear time 과 constant space 로 찾을 수 있는 알고리즘이다.

참고로 Boyer–Moore 문자열 검색 알고리즘(string-search algorithm)과는 다르므로 헷갈리지 말자.

보이어 무어 과반수 투표 알고리즘은 스트리밍 알고리즘(streaming algorithm)의 대표적인 예다.

만약 배열 내 과반수(절반이 넘는 수)에 해당하는 원소가 존재한다는 보장이 된다면, 결과값은 항상 과반수 원소가 된다.

주의할 점은, 만약 배열 내에 과반수 만큼 등장하는 원소가 없다면 결과값으로 임의의 의미없는 값이 나오게 된다(딱 절반 만큼 등장하는 원소가 있더라도 마찬가지다)

즉, 과반수 만큼 등장하는 원소가 있다는 보장이 없다면, 결과값이 항상 과반수에 해당하는 원소라는 보장도 없다는 것이다.
