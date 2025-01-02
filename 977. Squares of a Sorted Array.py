class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        l, r = 0, len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.append(left**2)
                l+=1
            else:
                answer.append(right**2)
                r-=1
        return answer[::-1]
        