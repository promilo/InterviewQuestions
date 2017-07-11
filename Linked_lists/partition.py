''' Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -) 5 -) 8 -) 5 -) 113 -) 2 -) 1 [partition = 5]
Output: 3 -) 1 -) 2 -) 113 -) 5 -) 5 -) 8 '''

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

def partition(node, x):
    before = None
    beforeHead=None
    after = None
    afterHead = None
    while node:
        if node.data < x:
            if before:
                before.next = node
                before = before.next
            else:
                before = node
                beforeHead = before
            node = node.next
        else:
            if after:
                after.next = node
                after = after.next
            else:
                after = node
                afterHead = after
            node = node.next
    before.next = afterHead
    print_list(beforeHead)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(2)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    partition(node1, 3)
