class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class StackQueue:
     def __init__(self):
         self.newStack = Stack()
         self.oldStack = Stack()

     def isEmpty(self):
         return self.newStack.isEmpty() or self.oldStack.isEmpty()

     def push(self, item):
         if self.oldStack.isEmpty():
             while not self.newStack.isEmpty():
                 self.oldStack.push(self.newStack.pop())
         self.newStack.push(item)

     def pop(self):
         if self.oldStack.isEmpty():
             while not self.newStack.isEmpty():
                 self.oldStack.push(self.newStack.pop())
         return self.oldStack.pop()

     def peek(self):
         if self.oldStack.isEmpty():
             while not self.newStack.isEmpty():
                 self.oldStack.push(self.newStack.pop())
         return self.oldStack.peek()

if __name__ == '__main__':

    myQueue = StackQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    print myQueue.pop()
    print myQueue.pop()
