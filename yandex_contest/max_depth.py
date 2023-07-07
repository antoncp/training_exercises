# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False
DEPTH = 0

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root, d=1) -> int:
    global DEPTH
    if d > DEPTH:
        DEPTH = d
    if root.right:
        solution(root.right, d + 1)
    if root.left:
        solution(root.left, d + 1)
    return DEPTH


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4) 
    assert solution(node5) == 3


if __name__ == '__main__':
    test()