#implement a tree

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,leftNode):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[])
    else:
        root.insert(1,[leftNode,[],[]])
    pass

def insertRight(rightNode):
    pass