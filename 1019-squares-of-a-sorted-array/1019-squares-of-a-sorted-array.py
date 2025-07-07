class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       y=[]
       for i in range(len(nums)):
        r=nums[i]*nums[i]
        y.append(r)
        y.sort()
       return y
        