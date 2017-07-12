''' Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack. '''


# To solve this we are goin to use list of lists where very list could act as a stack
class Stack:
     def __init__(self, maxi):
         self.items = [[]]
         self.max = maxi
         self.stackIndex = 0
     def isEmpty(self):
         return self.items == []

     def push(self, item):
         if len(self.items[self.stackIndex]) <= self.max:
             self.items[self.stackIndex].append(item)
             print "self.items after push", self.items
         else:
             if self.items[self.stackIndex] == []:
                 self.items[self.stackIndex].append(item)
                 self.stackIndex += 1
                 print "self.items after push", self.items
             else:
                 self.items.append([item])
                 self.stackIndex += 1
                 print "self.items after push", self.items


     def pop(self):
         popped = self.items[self.stackIndex].pop()
         if self.items[self.stackIndex] == []:
             self.stackIndex -= 1
         print "self.items after pop", self.items
         return popped

     def peek(self):
         return self.items[len(self.items)-1]


if __name__ == '__main__':
    plate = Stack(2)
    plate.push(3)
    plate.push(2)
    plate.push(5)
    plate.push(4)
    plate.push(6)
    print plate.pop()
    print plate.pop()
    print plate.pop()
