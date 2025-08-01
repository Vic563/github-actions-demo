import unittest
import sys
import os

# Add the current directory to the path so we can import coin_flip
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import coin_flip

class TestCoinFlip(unittest.TestCase):
    """Test cases for the coin flip program"""
    
    def test_flip_coin_returns_valid_values(self):
        """Test that flip_coin() returns either 'Heads' or 'Tails'"""
        result = coin_flip.flip_coin()
        self.assertIn(result, ['Heads', 'Tails'])
    
    def test_flip_coin_probability(self):
        """Test that flip_coin() produces roughly equal distribution over many flips"""
        heads_count = 0
        tails_count = 0
        
        # Perform 1000 flips to check distribution
        for _ in range(1000):
            result = coin_flip.flip_coin()
            if result == 'Heads':
                heads_count += 1
            else:
                tails_count += 1
        
        # Check that neither side has less than 40% (allowing for randomness)
        total = heads_count + tails_count
        heads_percentage = (heads_count / total) * 100
        tails_percentage = (tails_count / total) * 100
        
        self.assertGreater(heads_percentage, 40)
        self.assertGreater(tails_percentage, 40)
    
    def test_main_runs_without_error(self):
        """Test that the main function runs without errors"""
        try:
            coin_flip.main()
            main_ran_successfully = True
        except Exception as e:
            main_ran_successfully = False
            print(f"Main function failed with error: {e}")
        
        self.assertTrue(main_ran_successfully)

if __name__ == '__main__':
    unittest.main()
