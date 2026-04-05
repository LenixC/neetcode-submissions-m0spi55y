class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have:
        #    list of nums, a target int
        # want:
        #    indices of two numbers that add to target [a, b]

        num_pos_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_pos_dict:
                return [num_pos_dict[diff], i]
            
            num_pos_dict[num] = i
