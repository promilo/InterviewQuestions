'''  Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? '''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def remove_dups(node):
    unique = []
    unique.append(node.data)
    prevNode = node
    node = node.next
    while node != None :
        if node.data in unique:
            prevNode.next = node.next
            prevNode = node.next
            node = node.next
        else:
            unique.append(node.data)
            prevNode = node
            node = node.next

def print_list(node):
    while node:
        print node,
        node = node.next
    print


if __name__ == '__main__':
    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('2')
    node1.next = node2
    node2.next = node3
    print_list(node1)
    remove_dups(node1)
    print_list(node1)
