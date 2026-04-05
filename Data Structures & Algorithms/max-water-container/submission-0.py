def calc_area(h1, h2, w):
    return min(h1, h2) * w

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                area = calc_area(h1, h2, j-i)
                if area > max_area:
                    max_area = area
        
        return max_area