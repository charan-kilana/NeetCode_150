class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums)>=2 and len(nums)<=1000):
            for i in range(0,len(nums)):
                for j in range(0,len(nums)):
                    # if(nums[i]==nums[j]):
                    #     continue
                    # else:
                    if(i==j):
                        continue
                    else:
                        if(nums[i]+nums[j])==target:
                            return [i, j]
