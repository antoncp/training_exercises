# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head.next:
            nodes.append(head)
            head = head.next
        nodes.append(head)
        mid = len(nodes) // 2
        return nodes[mid]
