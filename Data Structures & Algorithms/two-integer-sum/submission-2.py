class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = dict()
        
        for i, num in enumerate(nums):
            if num in targets.keys(): 
                return [targets[num], i]
            targets[target - num] = i
        
        return targets

