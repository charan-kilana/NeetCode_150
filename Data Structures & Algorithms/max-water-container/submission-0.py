class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force Method
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area = (j-i)*min(heights[i], heights[j])
                if area > max_area:
                    max_area = area
        return max_area