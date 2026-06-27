class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        internal = enumerate(nums)

        for i, num in internal:
            missing ^= i ^ num
        
        return missing 