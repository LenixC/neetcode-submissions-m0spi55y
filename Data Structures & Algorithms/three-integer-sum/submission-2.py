class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 out = sorted([nums[i], nums[j], nums[k]])
        #                 if out not in res:
        #                     res.append(out)
        # return res

        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]: # Don't repeat the same num
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

