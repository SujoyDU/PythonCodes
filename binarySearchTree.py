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

    def findNode(self,val):
        if self.data > val:
            if self.leftChild is None:
                print("value not found")
                return None
            else:
                return self.leftChild.findNode(val)
        elif self.data < val:
            if self.rightChild is None:
                print("value not found")
                return None
            else:
                return self.rightChild.findNode(val)
        
        else: 
            print("value is found")
            self.findPath(self)
            print()
            return self

            
    def findPath(self, node):
        if node.parent is None:
            print(node.data, end = "")
            return
        else:
            self.findPath(node.parent)
            print(f' --> {node.data}', end=" ")
        
        
    def deleteNode(self, val):
        node  = self.findNode(val)
        if node is None:
            return
        else:
            if node.leftChild is None and node.rightChild is None:
                parentNode = node.parent
                if parentNode.leftChild is node:
                    parentNode.leftChild = None
                else: parentNode.rightChild = None
                del node
            
            elif node.leftChild is not None and node.rightChild is not None:
                successorNode = node.rightChild
                while successorNode.leftChild is not None:
                    successorNode = successorNode.leftChild
                
                parentNode = successorNode.parent
                if parentNode.leftChild is successorNode:
                    parentNode.leftChild = None
                else: parentNode.rightChild = None

                node.data = successorNode.data 
                node.rightChild = successorNode.rightChild
                if successorNode.rightChild is not None:
                    successorNode.rightChild.parent = node

                del successorNode

                



            else:
                if node.leftChild is not None:
                    childNode = node.leftChild
                    node.data = childNode.data
                    node.leftChild = childNode.leftChild
                    node.rightChild = childNode.rightChild
                    del childNode
                else:
                    childNode = node.rightChild
                    node.data = childNode.data
                    node.leftChild = childNode.leftChild
                    node.rightChild = childNode.rightChild
                    del childNode




                


    def printInorder(self):
        if self.leftChild is not None:
            self.leftChild.printInorder()
        print(self.data)
        if self.rightChild is not None:
            self.rightChild.printInorder()
        

if __name__ == ('__main__'):
    x = Node(7)
    x.insert(10)
    x.insert(5)
    x.insert(4)
    x.insert(1)
    x.insert(12)
    x.insert(15)
    x.insert(18)
    x.insert(17)
    x.insert(20)
    x.insert(16)
    x.printInorder()
    x.findNode(16)
    x.deleteNode(17)

    # x.deleteNode(18)   
    x.printInorder()
    x.findNode(16)

    
    
     

   