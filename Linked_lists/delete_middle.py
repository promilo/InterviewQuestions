''' Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.'''

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
# this will only delete from the second node of the linked list
def delete (node):
    node.next = node.next.next


if __name__ == '__main__':
    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('4')
    node4 = Node('a')
    node5 = Node('5')
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    delete(node1)
    print_list(node1)
