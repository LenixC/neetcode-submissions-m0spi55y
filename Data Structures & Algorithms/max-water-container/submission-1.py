def calc_area(h1, h2, w):
    return min(h1, h2) * w

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0
        
        # for i, h1 in enumerate(heights):
        #     for j, h2 in enumerate(heights):
        #         area = calc_area(h1, h2, j-i)
        #         if area > max_area:
        #             max_area = area
        
        # return max_area
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            res = max(res, calc_area(heights[l], heights[r], r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
