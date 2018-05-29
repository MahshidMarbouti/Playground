import unittest
from Fedex import fedex
from ShippingCost import Shipping

class TestMethods(unittest.TestCase):
    def test_shipping_cost_fedex(self):
        #ship by fedex
        fedex_order = fedex()
        fedex_shipping= Shipping(fedex_order)
        self.assertEqual(fedex_shipping.calculate(), 4)
        
if __name__ == '__main__':
    unittest.main()
