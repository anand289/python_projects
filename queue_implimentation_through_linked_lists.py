class Queue:

  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    return self.first
  
  def enqueue(self,value):
    self.node = {
      'value':value,
      'next':None
    }
    if self.length == 0:
      self.first = self.node
      self.last = self.node
    else:
      self.last['next'] = self.node 
      self.last = self.node
    self.length = self.length + 1

  
  def dequeue(self):
    self.first = self.first['next']
    self.length = self.length - 1

  def print_queue(self):
    arr = []
    current_node = self.first
    counter = self.length
    while counter > 0:
      arr.append(current_node['value'])
      current_node = current_node['next']
      counter = counter - 1
    return print(arr)



Q1 = Queue()
print(Q1.peek())
Q1.enqueue(1)
Q1.enqueue(2)
Q1.enqueue(3)
Q1.enqueue(4)

print(Q1.length)
print(Q1.first)
print(Q1.last)
print(Q1.peek())

Q1.print_queue()
Q1.dequeue()
print(Q1.length)
print(Q1.first)
print(Q1.last)
print(Q1.peek())

Q1.print_queue()

#1 comes in first goes out first.



    


  




