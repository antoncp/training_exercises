# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n, l1_values = l1, str(l1.val)
        while n.next:
            l1_values += str(n.next.val)
            n = n.next
        n, l2_values = l2, str(l2.val)
        while n.next:
            l2_values += str(n.next.val)
            n = n.next
        new_list_values = list(str(sum([int(l1_values[::-1]), int(l2_values[::-1])])))[::-1]
        last_node = ListNode(val=int(new_list_values[0]))
        head = last_node
        for value in new_list_values[1:]:
            new_node = ListNode(val=int(value))
            last_node.next = new_node
            last_node = new_node
        return head
