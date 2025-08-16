import unittest

# Global thresholds (avoid magic numbers)
BULKY_VOLUME_THRESHOLD_CM3: float = 1000000.0
BULKY_DIMENSION_THRESHOLD_CM: float = 150.0
HEAVY_MASS_THRESHOLD_KG: float = 20.0


def sort(width: float, height: float, length: float, mass: float) -> str:
    
    try:
        f_width = float(width)
        f_height = float(height)
        f_length = float(length)
        f_mass = float(mass)
    except (TypeError, ValueError):
        raise TypeError("width, height, length, and mass must be numeric")

    if min(f_width, f_height, f_length, f_mass) <= 0:
        raise ValueError("Dimensions and mass must be positive")

    volume = f_width * f_height * f_length
    largest_dimension = max(f_width, f_height, f_length)
    
    is_bulky = (
        volume >= BULKY_VOLUME_THRESHOLD_CM3 
        or largest_dimension >= BULKY_DIMENSION_THRESHOLD_CM
    )
    
    is_heavy = f_mass >= HEAVY_MASS_THRESHOLD_KG

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


class TestSort(unittest.TestCase):
    def test_standard_small(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume_exact_threshold(self):
        # 100 * 100 * 100 = 1,000,000
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_by_dimension_exact_threshold(self):
        self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 150, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 1, 150, 1), "SPECIAL")

    def test_heavy_exact_threshold(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected_both_conditions(self):
        self.assertEqual(sort(150, 150, 1, 20), "REJECTED")

    def test_just_below_thresholds(self):
        # Volume below threshold
        self.assertEqual(sort(100, 100, 99, 10), "STANDARD")
        # Dimensions just below threshold
        self.assertEqual(sort(149.9, 10, 10, 10), "STANDARD")
        # Mass just below threshold
        self.assertEqual(sort(10, 10, 10, 19.99), "STANDARD")

    def test_zero_values_raise(self):
        with self.assertRaises(ValueError):
            sort(0, 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 0, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 0, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, 0)

    def test_negative_values_raise(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 1)
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 1)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)

    def test_non_numeric_raises(self):
        with self.assertRaises(TypeError):
            sort("a", 10, 10, 1)
        with self.assertRaises(TypeError):
            sort(10, None, 10, 1)
        with self.assertRaises(TypeError):
            sort(10, 10, 10, object())

    def test_numeric_strings_accepted(self):
        self.assertEqual(sort("150", "1", "1", "1"), "SPECIAL")  # bulky by dimension
        self.assertEqual(sort("10", "10", "10", "20"), "SPECIAL")  # heavy by mass
        self.assertEqual(sort("150", "150", "1", "20"), "REJECTED")  # both
        self.assertEqual(sort("10", "10", "9", "1"), "STANDARD")  # neither
