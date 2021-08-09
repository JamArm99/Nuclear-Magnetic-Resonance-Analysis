import unittest
import func_NMR
class TestNMR(unittest.TestCase):

    def test_radius(self):
        with self.assertRaises(ValueError):
            #theta variable can take any value as trig function; hence, 1
            func_NMR.radius(0,1)#0 radius is unphysical

    def test_b(self):
        with self.assertRaises(ValueError):
            #theta variable can take any value as trig function; hence, 1
            func_NMR.bx(1,0)#0 radius is unpyhsical
            func_NMR.by(1,0)#0 radius is unphysical

    def test_mag(self):
        #test size of lists returned when passing function
        Mx, My, Mz, time = func_NMR.Mag(1e-7,0.001,10,0.001)
        self.assertEqual(len(time),10/0.001)#Max time divided by iteration

        with self.assertRaises(ValueError):
            func_NMR.Mag(0,1,1,1)#No NMR effects if transverse field is 0
            func_NMR.Mag(1,1,0,1)#End time cannot be 0
            func_NMR.Mag(1,1,1,0)#Iteration cannot be 0
            func_NMR.Mag(0,1,0,0)#Test all 3 unphysical values

#Running unittest directly in terminal/editor
if __name__ == '__main__':
    unittest.main()
#Default is python3 -m unittest test_NMR.py