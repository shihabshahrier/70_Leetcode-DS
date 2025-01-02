class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        s = sorted(list(nums))
        d = {}
        for i, v in enumerate(s):
            if v not in d:
                d[v] = i
        for i in nums:
            ans.append(d[i])
        return ans