class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = []
        for num in nums:
            if num in nums_2:
                return True
            
            nums_2.append(num)
        return False