class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = set()
        for num in nums:
            if num in nums_2:
                return True
            
            nums_2.add(num)
        return False