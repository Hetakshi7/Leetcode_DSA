class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mp = {0:-1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            r = total%k
            if r in mp:
                if i-mp[r]>=2:
                    return True
            else: 
                mp[r] = i
        return False
        