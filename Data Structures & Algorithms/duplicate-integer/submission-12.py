class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force method
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                return True
        return False

        # dict1 = {}
        # for i in nums:
        #     if(i in dict1):
        #         return True
        #     dict1[i] = 1
        # return False

