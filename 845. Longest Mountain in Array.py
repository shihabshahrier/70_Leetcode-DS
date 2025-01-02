class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        i = 1
        ln = len(arr)-1
        while i < ln:
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
            
                while l > 0 and arr[l] > arr[l-1]:
                    l-=1
                while r < ln and arr[r] > arr[r+1]:
                    r+=1
                ans = max(ans, r-l+1)
                i = r
            else:
                i += 1 
        return ans