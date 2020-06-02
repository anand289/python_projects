class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,value):
    self.node= {
      'value':value,
      'next':None
    }
    if self.length == 0:
      self.top = self.node
      self.bottom = self.node
      self.length = self.length + 1
    else:
      self.node['next'] = self.top
      self.top = self.node
      self.length = self.length + 1

  def pop(self):
    self.top = self.top['next']
    self.length = self.length - 1

  def peek(self):
    print(self.top['value'])

  def print_stack(self):
    arr = []
    current_node = self.top
    counter = self.length
    while counter > 0:
      arr.append(current_node['value'])
      current_node = current_node['next']
      counter = counter - 1
    return print(arr)

S1 = Stack()
S1.push(6)
S1.push(9)
print(S1.top)
print(S1.bottom)
S1.print_stack()
print(S1.length)


