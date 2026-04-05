class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [x for xs in matrix for x in xs]

        l, r = 0, len(flat) - 1

        while l <= r:
            print(flat[l:r])
            m = l + (r - l) // 2
            print(flat[m])
            if flat[m] < target:
                l = m + 1
            elif flat[m] > target:
                r = m - 1
            else:
                return True
        return False
