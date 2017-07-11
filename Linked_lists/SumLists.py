''' Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .Thatis,617 + 295.
Output: 2 - > 1 - > 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
Output: 9 - > 1 - > 2. That is, 912. '''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def print_list(node):
    while node:
        print node,
        node = node.next
    print


def sumLists(node1, node2):
    carry = 0
    totalHead = None
    total = None
    while node1:
        if node1.next:
            val = node1.data + node2.data + carry
            print "val ", val
            if total:
                total.next = Node(val % 10)
                print "total next", total.next
                if totalHead.next == None:
                    totalHead.next = total
                total = total.next

            else:
                total = Node(val % 10)
                totalHead = total
            if val > 9:
                carry = 1
            else:
                carry = 0
        else:
            if node1.data + node2.data + carry > 9:
                total.next = Node((node1.data + node2.data + carry ) % 10)
                total.next.next = Node(1)
            else:
                total.next = Node(node1.data + node2.data)
        print "total", total
        print "node1 data", node1.data
        print "node2 data", node2.data
        node1 = node1.next
        node2 = node2.next
    print_list(totalHead)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(2)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6
    sumLists(node1, node4)
