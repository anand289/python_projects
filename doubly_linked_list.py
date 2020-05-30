class DLL:
  def __init__(self,value):
    self.head = {
      'value':value,
      'next':None,
      'previous':None
    }
    self.tail = self.head
    self.length = 1 

  def append(self,value):
    self.node = {
      'value':value,
      'next':None,
      'previous':None
    }
    self.tail['next'] = self.node
    self.node['previous'] = self.tail
    self.tail = self.node
    self.length = self.length + 1

  def prepend(self,value):
    self.node = {
      'value':value,
      'next':None,
      'previous':None
    }
    self.node['next'] = self.head
    self.head['previous'] = self.node
    self.head = self.node
    self.length = self.length + 1

  def print_list(self):
    arr = []
    current_node = self.head
    while current_node != None:
      arr.append(current_node['value'])
      current_node = current_node['next']
    print(arr)

  def traverse_to_index(self,index):
    if index <= self.length/2:
      current_node = self.head
      counter = 0
      while counter < index:
        current_node = current_node['next']
        counter = counter + 1
      return current_node
    else:
      current_node = self.tail
      counter = self.length - 1
      while counter > index:
        current_node = current_node['previous']
        counter = counter - 1
      return current_node

  def insert(self,index,value):
    self.node = {
      'value':value,
      'next':None,
      'previous':None
    }
    leader = self.traverse_to_index(index-1)
    follower = leader['next']
    leader['next'] = self.node
    self.node['next'] = follower
    self.node['previous'] = leader
    follower['previous'] = self.node
    self.length = self.length + 1

  def remove(self,index):
    current_node = self.traverse_to_index(index)
    next_node = current_node['next']
    previous_node = current_node['previous']
    next_node['previous'] = previous_node
    previous_node['next'] = next_node

    

    


myDLL = DLL(10)
myDLL.append(3)
myDLL.prepend(7)
myDLL.append(2)
myDLL.prepend(5)
myDLL.print_list()
myDLL.insert(2,15)
myDLL.print_list()
myDLL.remove(3)
myDLL.print_list()


