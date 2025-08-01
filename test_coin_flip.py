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
    
    def test_calculate_statistics(self):
        """Test that calculate_statistics returns correct values"""
        # Test with 60 heads, 40 tails, 100 flips
        stats = coin_flip.calculate_statistics(60, 40, 100)
        
        self.assertEqual(stats['heads_percentage'], 60.0)
        self.assertEqual(stats['tails_percentage'], 40.0)
        self.assertEqual(stats['heads_diff'], 10.0)
        self.assertEqual(stats['tails_diff'], -10.0)
        
        # Standard deviation for 100 flips should be 5.0
        self.assertAlmostEqual(stats['std_dev'], 5.0, places=1)
        
        # Z-score should be 2.0 (10 / 5)
        self.assertAlmostEqual(stats['z_score'], 2.0, places=1)
        
        # With z-score of 2.0, significance should be "unusual - might indicate bias"
        self.assertEqual(stats['significance'], "unusual - might indicate bias")
    
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
