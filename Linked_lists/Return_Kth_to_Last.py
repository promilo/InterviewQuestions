''' Return Kth to last '''
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

def kth (node, k):
    prevNode = node
    node = node.next
    counter = 0
    while counter < k:
        if node.next is None:
            return "Out of Bounds"
        else:
            counter += 1
            if counter == k:
                prevNode.next = None
                return print_list(node)
            else:
                prevNode = node
                node = node.next


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
    kth(node1, 2)
