from Node import Node
from Node import link_list
import unittest

class list_advanced_operations():
    def __init__(self):
        pass
    def remove_duplicates(self, list):
        dict = {}
        for node in list.iterate():
            if self.insert(node.value, dict)== True:
                if node == list.head:
                    list.head = node.next
                    node.next.previous = node.previous
                elif node ==list.tail:
                    list.tail = node.previous
                    node.previous.next = node.next
                else:
                    node.next.previous = node.previous
                    node.previous.next = node.next
                
                    
                     
    def insert(self, item, dict):
        if item in dict.keys():
            return True
        else:
            dict[item] = True
        return False


class TestMethods(unittest.TestCase):
    def test_remove_duplicates(self):
        l2 = link_list()
        l2.add_to_head(Node(5))
        l2.add_to_head(Node(8))
        l2.add_to_head(Node(5))
        l2.add_to_head(Node(4))
        print(l2.traverse())
        op = list_advanced_operations()
        op.remove_duplicates(l2)
        print(l2.traverse())

        l2 = link_list()
        l2.add_to_head(Node(4))
        print(l2.traverse())
        op = list_advanced_operations()
        op.remove_duplicates(l2)
        print(l2.traverse())


if __name__ == '__main__':
    unittest.main()