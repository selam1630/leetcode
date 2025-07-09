from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_map = {0: -1}  # remainder -> index

        for i, num in enumerate(nums):
            prefix_sum += num  # ✅ use num, not i!
            j = prefix_sum % k

            if j in prefix_map:
                if i - prefix_map[j] >= 2:
                    return True
            else:
                prefix_map[j] = i  # only set if first time seeing this remainder

        return False
