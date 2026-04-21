class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = 0
        for i in range(k):
            if blocks[i] == 'W':
                count_w += 1

        # j = [i - k]
        # W W B B B W B B W ==== 4
        # j - - - i . . . . ==== 
        # . j - - - i . . . 
        res = count_w
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count_w -= 1
            if blocks[i] == 'W':
                count_w += 1
            res = min(res, count_w)
        
        return res