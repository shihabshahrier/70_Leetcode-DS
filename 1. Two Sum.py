class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        dic = {nums[i]:i for i in range(l)}
        for i in range(l):
            t = target - nums[i]
            if t in dic and dic[t] != i:
                return [i, dic[t]]