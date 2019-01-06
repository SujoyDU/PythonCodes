class Node:
    def __init__(self,val = None):
        self.parent = None
        self.data = val
        self.leftChild = None
        self.rightChild = None

    def insert(self,val):
        if self.data is None:
            self.data = val
        else:
            if(self.data > val):
                if self.leftChild is None:
                    self.leftChild = Node(val)
                    self.leftChild.parent = self
                else: 
                    self.leftChild.insert(val)

            elif (self.data < val):
                if self.rightChild is None:
                    self.rightChild = Node(val)
                    self.rightChild.parent = self
                else: 
                    self.rightChild.insert(val)

    def search(self,val):
        if self.data > val:
            if self.leftChild is None:
                print("value not found")
            else:
                self.leftChild.search(val)
        elif self.data < val:
            if self.rightChild is None:
                print("value not found")
            else:
                self.rightChild.search(val)
        
        else: 
            print("value is found")
            self.findPath(self)
            print()

            
    def findPath(self, node):
        if node.parent is None:
            print(node.data, end = " ")
            return
        else:
            self.findPath(node.parent)
            print(f'--> {node.data}', end=" ")
        
        
        



            

    def printInorder(self):
        if self.leftChild is not None:
            self.leftChild.printInorder()
        print(self.data)
        if self.rightChild is not None:
            self.rightChild.printInorder()
        

if __name__ == ('__main__'):
    x = Node(7)
    x.printInorder()
    y = Node()
    x.insert(10)
    x.insert(5)
    x.insert(4)
    x.insert(1)
    x.insert(12)
    x.insert(15)
    x.insert(18)
    x.insert(17)
    x.insert(20)

    x.printInorder()
    x.search(15)

    y.insert(6)
    y.printInorder()
        
