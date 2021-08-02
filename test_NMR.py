import unittest
import func_NMR
import numpy as np

class TestNMR(unittest.TestCase):

    def test_radius(self):
        with self.assertRaises(ValueError):
            func_NMR.radius(0)#0 radius is unphysical


#Running unittest directly in terminal/editor
if __name__ == '__main__':
    unittest.main()
#Default is python3 -m unittest test_spdc_g2.py