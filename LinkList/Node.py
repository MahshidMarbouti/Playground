import unittest
class Node():
    def __init__(self, value=None):
        self.value= value
        self.next = None


class link_list():
    def __init__(self, node= None):
        self.head = self.tail = node
        if node!= None:
            self.count= 1
        else:
            self.count= 0
        
        
    def add_to_head(self, node):
        if self.is_empty():
            self.insert_first(node)
        else:
            node.next = self.head
            self.head = node
        self.count+=1

    def remove_from_head (self):
        if not (self.is_empty()):
            self.head = self.head.next
            self.count-=1


    def add_to_tail(self,node):
        if self.is_empty():
            self.insert_first(node)
        else:
            self.tail.next= node
            self.tail= node
        self.count+=1

    def remove_from_last(self, node):
        if not (self.is_empty()):
            current = self.head
            while current != tail :
                current= current.next
            current.next = None
            self.tail = current
            self.count-=1    

    def traverse(self):
        pointer = self.head
        result= []
        while  pointer != None:
            result.append( pointer.value)
            pointer = pointer.next
        return result

    def get_enumerator(self):
        pass

    def is_empty(self):
        if self.count==0:
            return True
        else:
            return False

    def insert_first(self, node):
        if self.is_empty():
            self.head = self.tail= node
        else:
            print("ERROR, LIST NOT EMPTY")    

class TestMethods(unittest.TestCase):
    def test_node_empty(self):
        l1 = link_list()
        self.assertEqual(l1.traverse(), [])
    def test_node(self):
        n1 = Node(4)
        l2 = link_list(n1)
        self.assertEqual(l2.traverse(), [4])
        l2.add_to_head(Node(5))
        l2.add_to_head(Node(8))
        self.assertEqual(l2.traverse(), [8,5,4])
    def test_node_remove(self):
        n1 = Node(4)
        l2 = link_list(n1)
        l2.add_to_head(Node(5))
        l2.add_to_head(Node(8))
        self.assertEqual(l2.traverse(), [8,5,4])
        l2.remove_from_head()
        self.assertEqual(l2.traverse(), [5,4])

if __name__ == '__main__':
    unittest.main()