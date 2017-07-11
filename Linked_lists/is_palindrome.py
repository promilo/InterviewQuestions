# Palindrome: Implement a function to check if a linked list is a palindrome.
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

def reverse(node):
    head = None
    while node:
        output = Node(node.data)
        output.next = head
        head = output
        node = node.next
    return head

def is_palindrome(node):
    rev = reverse(node)
    if rev.data == node.data:
        rev = rev.next
        node = node.next
    else:
        return False
    return True













if __name__ == '__main__':
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('d')
    node4 = Node('d')
    node5 = Node('b')
    node6 = Node('a')
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print is_palindrome(node1)
