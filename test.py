import unittest
from elevator import *

class TestMethods(unittest.TestCase):
    def test_constructor_set_invalid_door_status(self):
        #arrange
        with self.assertRaises(ValueError):
            e = Elevator(1, "D", 0, 10)
    def test_constructor_set_invalid_current_floor(self):
        #arrange
        with self.assertRaises(ValueError):
            e = Elevator(-1, "C", 0, 10)
    def test_constructor_invalid_current_floor(self):
        #arrange
        e = Elevator(1, "C", 0, 10)
        self.assertEqual(e.currentFloor, 1)
    def test_travese_traverse_correctly(self):
        e = Elevator(1, "C", 0, 10)
        e.traverse(8)
        self.assertEqual(e.currentFloor, 8)
        e.traverse(4)
        self.assertEqual(e.currentFloor, 4)
        e.traverse(10)
        self.assertEqual(e.currentFloor, 10)

    def test_travese_check_boundary(self):
        e = Elevator(1, "C", 0, 10)
        e.traverse(10)
        self.assertEqual(e.currentFloor, 10)

    def test_travese_check_invalid_floor(self):
        e = Elevator(1, "C", 0, 10)
        with self.assertRaises(ValueError):
            e.traverse(11)
        
if __name__ == '__main__':
    unittest.main()