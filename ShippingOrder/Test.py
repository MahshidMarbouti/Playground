import unittest

class Test(unittest.testcases):
    def test_shipping_cost_fedex():
        #ship by fedex
        fedex_order = fedex()
        fedex_shipping= Shipping(fedex_order)
        fedex_shipping.calculate()
        
