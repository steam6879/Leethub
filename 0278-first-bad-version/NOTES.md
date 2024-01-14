### Adjusted the initial values of left and right assuming versions start from 1.
1. Used (left + right) // 2 to calculate the mid-value to avoid integer overflow issues.
2. Simplified the logic to update left and right.
3. Removed the unnecessary check for isBadVersion(mid - 1) == False.
4. This should work correctly for finding the first bad version.

The key idea is to use a binary search to efficiently narrow down the range of versions until you find the first bad one.​


* 시간복잡도 : O(logN)
* 공간복잡도 : O(1)
