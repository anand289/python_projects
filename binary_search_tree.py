class BinarySearchTree:
  def  __init__(self):
    self.root = {
      'left' : None,
      'right' : None,
      'value' : None
    }

  def insert(self,value):
    self.node = {
      'left': None,
      'right' : None,
      'value' : value
    }
    if self.root['value'] == None:
      self.root = self.node
      return
    else:
      current_node = self.root
      while True:
        if value > current_node['value']:
          if current_node['right'] == None:
            current_node['right'] = self.node
            return
          else:
            current_node = current_node['right']
        elif value < current_node['value']:
          if current_node['left'] == None:
            current_node['left'] = self.node
            return
          else:
            current_node = current_node['left']

  def lookup(self,value):
    current_node = self.root
    while True:
      if current_node == None:
        return False
      if current_node['value'] == value:
        return True
      elif value < current_node['value'] :
        current_node = current_node['left']
      else:
        current_node = current_node['right'] 

  def print_tree(self):
    if self.root != None:
      self.printt(self.root)

  def printt(self,current_node):
    if current_node != None:
      self.printt(current_node['left'])
      print(str(current_node['value']))
      self.printt(current_node['right']) 
        

bst = BinarySearchTree()
bst.insert(9)
bst.insert(20)
bst.insert(4)
bst.insert(1)
bst.insert(15)
bst.insert(6)
bst.insert(170)

print(bst.lookup(20))
print(bst.lookup(21))
print(bst.lookup(29))
print(bst.lookup(4))
print(bst.lookup(9))

bst.print_tree()



    