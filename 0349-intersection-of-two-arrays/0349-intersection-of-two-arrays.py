class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        y=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in y:
                y.append(nums1[i])
        return y
        