# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        list_of_nodes = [head]
        while head.next:
            list_of_nodes.append(head.next)
            head = head.next
        del_node = list_of_nodes[-n]
        if (list_len := len(list_of_nodes)) > 1:
            if n < list_len:
                if del_node.next is not None:
                    list_of_nodes[-(n + 1)].next = list_of_nodes[-(n - 1)]
                else:
                    list_of_nodes[-(n + 1)].next = None
        del list_of_nodes[-n]
        return list_of_nodes[0] if list_of_nodes else None
