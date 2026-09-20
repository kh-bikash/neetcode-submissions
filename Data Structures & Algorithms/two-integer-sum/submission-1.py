class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimal Solution
        n=len(nums)
        seen={}
        for i in range(0,n):
            needed=target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i
        return []