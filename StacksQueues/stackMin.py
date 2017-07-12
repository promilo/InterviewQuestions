''' Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time. '''


class Stack:
    def __init__(self):
        self.items = []
        self.min = None
        self.minStack = []
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.min == None or item <= self.min:
            # print "push self.min", self.min
            self.minStack.append(item)
            # print "minStack after push", self.minStack
            self.min = item
        self.items.append(item)

    def pop(self):
        # print "Before pop", self.items
        popped = self.items.pop()
        # print "after pop", self.items
        if popped == self.min:
            # print "popped == self.min", self.min
            self.minStack.pop()
            # print "self.minStack after pop", self.minStack
            self.min = self.minStack[len(self.minStack) - 1]
        return popped

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def min(self):
        print self.minStack[len(self.minStack) - 1]

if __name__ == '__main__':

    new = Stack()
    new.push(9)
    print new.min
    new.push(8)
    print new.min
    new.push(10)
    print new.min
    print new.pop()
    print new.min
    print new.pop()
    print new.min
