class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        s = set(nums)
        for i in range(1, l+1):
            if i not in s:
                ans.append(i)
        return ans