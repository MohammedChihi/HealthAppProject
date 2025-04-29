import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.80, 80), 24.69, places=2)

    def test_calculate_bmr_male(self):
        bmr_male = calculate_bmr(180, 75, 25, "male")
        self.assertAlmostEqual(bmr_male, 1815.03, places=2)  # corrigé ici

    def test_calculate_bmr_female(self):
        bmr_female = calculate_bmr(165, 60, 30, "female")
        self.assertAlmostEqual(bmr_female, 1383.68, places=2)  # corrigé ici

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_bmr(165, 60, 30, "alien")

if __name__ == '__main__':
    unittest.main()