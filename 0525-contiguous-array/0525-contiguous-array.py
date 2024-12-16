from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0  # 누적 합 초기화
        hash_map = {0: -1}  # 누적 합이 처음 나타난 인덱스를 저장하는 해시 맵
        max_length = 0  # 최대 길이 초기화

        for i in range(len(nums)):
            # nums[i]가 0이면 -1을, 1이면 +1을 누적 합에 더함
            prefix_sum += -1 if nums[i] == 0 else 1

            if prefix_sum in hash_map:
                # 이전에 같은 누적 합이 있었다면, 그 인덱스부터 현재 인덱스까지의 길이 계산
                max_length = max(max_length, i - hash_map[prefix_sum])
            else:
                # 누적 합이 처음 등장하면 현재 인덱스를 해시 맵에 저장
                hash_map[prefix_sum] = i

        return max_length  # 가장 긴 부분 배열의 길이 반환
