import unittest

import lib.transfer_matrix

class TestTransferMatrix(unittest.TestCase):
    def test_calculate_transfer_matrix_drift(self):
        """
        Test the transfer matrix calculation for a drift yields analytical
        solution for a drift space        
        """
        self.assertTrue(False)

    def test_calculate_transfer_matrix_infinitesimal(self):
        """
        Test the transfer matrix calculation for an infinitesimal solenoid yields
        analytical solution
        """
        self.assertTrue(False)


    def test_calculate_transfer_matrix_constant(self):
        """
        Test the transfer matrix calculation for a constant solenoid yields
        analytical solution
        """
        self.assertTrue(False)

    def test_transport_phase_space_vector(self):
        """
        Test that the transport equations transport particle correctly    
        """
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()

