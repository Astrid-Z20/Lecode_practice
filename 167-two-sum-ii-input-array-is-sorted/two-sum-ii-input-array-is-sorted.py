class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result = {}
        for i, num in enumerate(numbers):
            another = target - num
            if another in result:
                return [result[another] + 1, i+1]
            else:
                result[num] = i