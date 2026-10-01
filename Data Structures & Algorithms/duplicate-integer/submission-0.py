class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count =  {}
        n = len(nums)
        for i, _ in enumerate(nums):
            count[nums[i]] = count.get(nums[i],0) + 1
        for val in count.values():
            if val != 1:
                return True
        return False