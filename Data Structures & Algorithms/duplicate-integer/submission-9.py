class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force method
        dict1 = {}
        for i in nums:
            if(i in dict1):
                return True
            dict1[i] = 1
        return False

