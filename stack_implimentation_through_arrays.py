#Stacks are better to impliment via arrays. Arrays(lists) in Python itseld act as stacks.

class Stack:
  def __init__(self):
    self.arr = []

  def push(self,value):
    value = self.arr.append(value)
    return value

  def pop(self):
    return self.arr.pop()

  def peek(self):
    return print(self.arr[len(self.arr)-1])

  def print_stack(self):
    return print(self.arr)


S1 = Stack()
S1.push(5)
S1.push(7)
S1.print_stack()
S1.peek()
S1.pop()
S1.print_stack()



