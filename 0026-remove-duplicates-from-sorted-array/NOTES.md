
# Two pointer
i와 j를 사용하여 두가지 변수를 통해 two pointer방식을 구현

# In-place Algorithm
```python3
                nums[j] = nums[i]
```
을 이용하여 새로운 list를 도입하는 것이 아닌 초기 입력받은 nums를 계속 수정하며 진행.



> In-place 알고리즘이란 원소들의 개수에 비해서 충분히 무시할 만한 저장 공간만을 더 사용하는 정렬 알고리즘. 아마 학교에서는 제자리성(혹은 제자리 정렬)과 같은 이름으로 들어봤을 수도 있겠다. (출처: 위키피디아)
> 
> 헷갈리면 정렬들을 공부하다보면 이해가 될 것이니 일단은 추가적인 메모리 공간이 거의(아예가 아니다) 안 드는 정렬이라고만 알고 있자.
>
>대표적인 알고리즘들
>
>In-place Sorting 알고리즘
>
>* Insertion Sort
>* Selection Sort
>* Bubble Sort
>* Shell Sort
>* Heap Sort
>* Quick Sort(정렬 알고리즘-4.2: 정의에 따라서 Not in place sorting으로 볼 수도 있으나 흔히 In-place로 본다.)
>
>Not in place Sorting 알고리즘
>
>* Merge Sort
>* Counting Sort
>* Radix Sort
>* Bucket Sort

***

* Time complexity : O(N)

* 해결 할 수 있는 방법은 많겠지만, **in place** 방식으로 구현해야 한다는 것에 주목하자.

***

# sort in place using [:]

```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
```
```nums =``` doesn't replace elements in the original list.

```nums[:] =``` replaces element in place

In short, without [:], we're creating a new list object, which is against what this problem is asking for:
"Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."
