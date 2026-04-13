class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        i = 0

        while i < len(nums):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                    return True
            hashmap[nums[i]] = i
            i += 1

        return False


        #i = 0
        #while i < len(nums):
        #    j = i+1
        #    while j <= i + k and j < len(nums):
        #        if nums[i] == nums[j]:
        #            return True
        #        
        #        j += 1
        #    i += 1
        #    
        #return False