class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r:
                curr_sum = v + nums[l] + nums[r]

                if curr_sum > 0:
                    r -= 1

                elif curr_sum < 0:
                    l += 1
                
                else:
                    triplet.append([v, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return triplet
