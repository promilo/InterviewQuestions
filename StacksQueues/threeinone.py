# Three in One: Describe how you could use a single array to implement three stacks.

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

class threeInOne:
     def __init__(self, size):
         # 3 is the number of stacks
         self.items = [0] * (size * 3)
         self.stackLengths = [0] * 3
         self.size = size

     def isEmpty(self, stackNum):
         return self.stackLengths[stackNum] == 0

     def isFull(self, stackNum):
        return self.stackLengths[stackNum] == self.size

     def push(self, item, stackNum):
         if self.isFull(stackNum):
             raise Exception('stack full')
         self.items[stackNum * 3 + self.stackLengths[stackNum]] = item
         self.stackLengths[stackNum] += 1
         print "The stack after push", self.items


     def pop(self, stackNum):
         if self.isEmpty(stackNum):
             raise Exception('stack empty')
         popped = self.items[stackNum * 3 + self.stackLengths[stackNum] - 1]
         self.items[stackNum * 3 + self.stackLengths[stackNum] - 1] = 0
         self.stackLengths[stackNum] -= 1
         print "The stack after pop", self.items
         return popped

     def peek(self, stackNum):
         if self.isEmpty(stackNum):
             raise Exception('stack empty')
         return self.items[stackNum * 3 + self.stackLengths[stackNum] - 1]

     def size(self):
         return len(self.items)


if __name__ == '__main__':

    new = threeInOne(2)
    print new.isEmpty(1)
    new.push(3, 1)
    print new.peek(1)
    print new.isEmpty(1)
    new.push(2, 1)
    print new.peek(1)
    print new.pop(1)
    print new.peek(1)
    new.push(3, 1)
