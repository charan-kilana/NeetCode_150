class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # BFM
        lis_set = set(nums)
        output = 0

        for i in lis_set:
            length = 1
            if i-1 not in lis_set:
                while(i+length in lis_set):
                    length += 1
            output = max(length, output)
        return output