import unittest
class Node():
    def __init__(self, value=None):
        self.value= value
        self.next = None


class link_list():
    def __init__(self, node= None):
        self.head = self.tail = node
        
    def add_to_head(self, node):
        if self.is_empty():
            self.head = self.tail= node
        else:
            node.next = self.head
            self.head = node

    def remove_from_head (self):
        if not (self.is_empty()):
            self.head = self.head.next

    def add_to_tail(self,node):
        pass

    def remove_from_last(self, node):
        pass    

    def traverse(self):
        pointer = self.head
        while  pointer != None:
            print(pointer.value, end=" ")
            pointer = pointer.next
        print()

    def get_enumerator(self):
        pass
    def is_empty(self):
        if self.head == None and self.tail==None:
            return True
        else:
            return False
        

class TestMethods(unittest.TestCase):
    def test_node_creation(self):
        l1 = link_list()
        n1 = Node(4)
        l2 = link_list(n1)
        l2.traverse()
        l2.add_to_head(Node(5))
        l2.add_to_head(Node(8))
        l2.traverse()
        l2.remove()
        l2.traverse()

if __name__ == '__main__':
    unittest.main()