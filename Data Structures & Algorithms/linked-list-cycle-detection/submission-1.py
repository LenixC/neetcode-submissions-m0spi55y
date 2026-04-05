# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = []
        if not curr:
            return False

        while curr.next is not None:
            if curr.val in visited:
                return True
            visited.append(curr.val)
            curr = curr.next
        return False