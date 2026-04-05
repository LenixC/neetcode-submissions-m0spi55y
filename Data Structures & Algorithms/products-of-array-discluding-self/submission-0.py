class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i, n in enumerate(nums):
            prod = 1
            for j, m in enumerate(nums):
                if i == j:
                    continue
                prod *= m
            res.append(prod)
        
        return res