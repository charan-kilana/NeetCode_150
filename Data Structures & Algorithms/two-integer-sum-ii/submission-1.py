class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] != numbers[j]:
                    if numbers[i] + numbers[j] == target:
                        if i not in output and j not in output:
                            output.append(i+1)
                            output.append(j+1)
        return output

