class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            h1 = stones.pop()
            h2 = stones.pop()

            broken = abs(h2 - h1)
            if broken > 0:
                stones.append(broken)
        
        if len(stones) == 0:
            return 0
        
        return stones[0]