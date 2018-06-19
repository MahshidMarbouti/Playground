from collections import deque
def min_depth(root):
    if root==None:
        return 0
    if root.right==None:
        return 1
    if root.left==None:
        return 1
    m = min(min_depth(root.right), min_depth(root.left))
    return m+1

def max_depth(root):
    if root==None:
        return 0
    if root.right==None and root.left==None:
        return 1
    if root.right==None:
        return max_depth(root.left) +1
    if root.left==None:
        return max_depth(root.right) +1
    m = max(max_depth(root.right), max_depth(root.left))
    return m+1
    
class Node():
    def __init__(self, value=None):
        self.value= value
        #self.parent = parent
        self.left = None
        self.right = None
    
class BST():
    def __init__(self, root = None):
        self.root= root

    def add(self,root, node):
        if root== None:
            root =node
        elif node.value < root.value:
            if root.left == None:  
                root.left = node
            else:
                self.add(root.left, node)   
        else:
            if root.right == None:  
                root.right = node
            else:
                self.add(root.right, node)
        

    def traverse(self, root):
        if root != None:
            list = deque([])
            #visited = {}
            current= root
            print(current.value)
            #visited[current.value]= 1
            list.append(current)
            while list:
                item= list.popleft()
                if item.left!= None:
                    print(item.left.value, end=" ")
                    list.append(item.left)
                if item.right!= None:
                    print(item.right.value, end=" ")
                    list.append(item.right)
                print()

T=BST(Node(value=1))
T.add(T.root, Node(2))
T.add(T.root, Node(4))
T.add(T.root, Node(3))
T.add(T.root, Node(8))
T.traverse(T.root)


print("min {0}".format(min_depth(T.root)))
print("max {0}".format(max_depth(T.root)))
