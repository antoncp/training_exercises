# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev_node = head
        while prev_node.next:
            if prev_node.val == prev_node.next.val:
                if prev_node.next.next:
                    prev_node.next = prev_node.next.next
                else:
                    prev_node.next = None
            else:
                prev_node = prev_node.next
        return head
