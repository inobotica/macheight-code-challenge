import unittest
from app import format_parameters, pair_integers

class TestParameters(unittest.TestCase):
    def test_missing_parameters(self):
        """
        Test correct number of parameters
        """
        params = ['app.py',0]
        result,_ = format_parameters(params)
        self.assertEqual(result, 0)
        
    def test_dataset_too_small(self):
        """
        Test dataset too small
        """
        params = ['app.py','0', '1']
        result,_ = format_parameters(params)
        self.assertEqual(result,1)
        
    def test_sum_outside_boundaries(self):
        """
        Test sum parameter outside boundaries
        """
        params = ['app.py','1,2,3', '10']
        result,_ = format_parameters(params)
        self.assertEqual(result, 2)

class TestPairIntegers(unittest.TestCase):
    def test_pairing_with_matches_found(self):
        """
        Test pairing function with matches found
        """
        integer_set = set([24,-5,-67,4,23,43,5,6,54,64,-56,1,23,9,8,7,12,14,15,161,-1,-2])
        total_sum = -3
        result = set([(-67,64),(-2, -1)])
        paired_integers = pair_integers(integer_set, total_sum)
        self.assertEqual(paired_integers, result)
    
    def test_pairing_with_matches_no_found(self):
        """
        Test pairing function with matches no found
        """
        integer_set = set([24,-5,-67,4,23,43,5,6,54,64,-56,1,23,9,8,7,12,14,15,161,-1,-2])
        total_sum = 200
        result = set()
        paired_integers = pair_integers(integer_set, total_sum)
        self.assertEqual(paired_integers, result)
        
if __name__ == '__main__':
    unittest.main()