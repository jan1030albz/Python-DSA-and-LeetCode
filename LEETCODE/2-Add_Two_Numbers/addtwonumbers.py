"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a
linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself."""

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
    def __str__(self) -> str:
        return self.data

a = ListNode("A")
b = ListNode("B")
c = ListNode("C")
d = ListNode("D")

a.next = b
b.next = c
c.next = d
d.next = None

def get_next(node):
    print(node)
    if node is not None:
        get_next(node.next)
        return node.next
    else:
        return None
    

get_next(a)
