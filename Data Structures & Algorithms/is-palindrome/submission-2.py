class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        p1 = 0
        p2 = len(s) - 1

        if len(s) == 0:
            return True

        while p1 < p2:
            #print(s[p1], s[p2])
            if s[p1].lower() != s[p2].lower():
                return False
            
            p1 += 1
            p2 -= 1
        return True
             