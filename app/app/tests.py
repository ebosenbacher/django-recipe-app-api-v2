"""
Sample unit tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_multiply_numbers(self):
        """Test multiplying numbers."""
        res = calc.multiply(3, 4)
        self.assertEqual(res, 12)
        