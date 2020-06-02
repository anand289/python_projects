#10-->5-->6

# myLL = {
#   'head':{
#     'value': 10,
#     'next': {
#       'value':5,
#       'next':{
#         'value' : 6,
#         'next': None
#       }
#     }
#   }
# }

class LL:
  def __init__(self,value):
    self.head = {
        'value': value,
        'next' : None   
    }
    self.tail = self.head
    self.length = 1

  def append(self,value):
    self.node = {
        'value': value,
        'next' : None   
    }
    self.tail['next'] = self.node
    self.tail = self.node
    self.length = self.length + 1

  def prepend(self,value):
    self.node = {
        'value': value,
        'next' : None   
    }
    self.node['next'] = self.head
    self.head = self.node
    self.length = self.length + 1

  def traverse_to_index(self,index):
    counter = 0
    current_node = self.head
    while counter != index:
      current_node = current_node['next']
      counter = counter + 1
    return current_node


  def insert(self,index,value):
    if (index >= self.length):
      print(f"Entered Index greater than the length. Adding element at the end." )
      return self.append(value)
    self.node = {
      'value': value,
      'next' : None
    }
    leader = self.traverse_to_index(index-1)
    holding_pointer = leader['next']
    leader['next'] = self.node
    self.node['next'] = holding_pointer
    self.length = self.length + 1
  

  def remove(self,index):
    before = self.traverse_to_index(index-1)
    after = self.traverse_to_index(index+1)
    before['next'] = after
    self.length = self.length - 1


  def print_list(self):
    current_node = self.head
    arr = []
    while current_node != None:
      arr.append(current_node['value'])
      current_node = current_node['next']
    return print(arr)

  def reverse(self):
   first = self.head
   second = first['next']
   while(second):
     temp = second['next']
     second['next'] = first
     first = second
     second = temp
   self.head['next'] = None
   self.head = first
       

myLL = LL(10)
myLL.append(5)
myLL.prepend(6)
myLL.append(3)
myLL.prepend(2)
myLL.print_list()
myLL.insert(3,7)
myLL.print_list()
myLL.remove(2)
myLL.print_list()
# print(myLL.head)
# print(myLL.tail)
# print(myLL.length)
myLL.reverse()
myLL.print_list()





