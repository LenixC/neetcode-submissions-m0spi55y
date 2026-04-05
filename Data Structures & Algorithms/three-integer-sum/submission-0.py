class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # want 4... (2, 1) = 1
        res = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out = sorted([nums[i], nums[j], nums[k]])
                        if out not in res:
                            res.append(out)
        return res