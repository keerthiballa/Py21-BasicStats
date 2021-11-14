import unittest
import formulas
import statistics
from scipy.stats import sem

class test_formulas(unittest.TestCase):

    def test_zcount(self):
        input = [1,2,3,4,5,6]
        expected = 6.0
        actual = formulas.zcount(input)
        self.assertEqual(expected,actual)

    def test_zmean(self):
        input=[1,2,3,4,5,6]
        expected = statistics.mean(input)
        actual = formulas.zmean(input)
        self.assertEqual(expected,actual)

    def test_zmedian_1(self):
        input=[1,2,3,4,5,6]
        expected = statistics.median(input)
        actual = formulas.zmedian(input)
        self.assertEqual(expected,actual)

    def test_zmedian_2(self):
        input=[1,2,3,4,5,6,7]
        expected = statistics.median(input)
        actual = formulas.zmedian(input)
        self.assertEqual(expected,actual)

    def test_zmode_1(self):
        input = [1,2,3,4,5.,5.,5.,6,6]
        expected = statistics.mode(input)
        actual =formulas.zmode(input)
        self.assertEqual(expected, actual)

    def test_zmode_2(self):
        input = [1, 2, 3, -4, 5., 5., 5., 6, 6]
        expected = statistics.mode(input)
        actual = formulas.zmode(input)
        self.assertEqual(expected, actual)

    def test_zvariance_1(self):
        input=[1,2,3,4,5,6]
        expected = statistics.variance(input)
        actual = formulas.zvariance(input)
        self.assertEqual(expected, actual)

    def test_zvariance_2(self):
        input = [1,2,3,4,5,6,7]
        expected = statistics.variance(input)
        actual = formulas.zvariance(input)
        self.assertEqual(expected, actual)

    def test_zstddev_1(self):
        input = [1,2,3,4,5,6]
        expected = statistics.stdev(input)
        actual = formulas.zstddev(input)
        self.assertEqual(expected, actual)

    def test_zstddev_2(self):
        input = [1,2,3,4,5,6,7]
        expected = statistics.stdev(input)
        actual = formulas.zstddev(input)
        self.assertEqual(expected, actual)

    def test_zstderr_1(self):
        input = [1, 2, 3, 4, 5, 6]
        expected = sem(input)
        actual = formulas.zstderr(input)
        self.assertEqual(expected, actual)

    def test_zstderr_2(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        expected = sem(input)
        actual = formulas.zstderr(input)
        self.assertEqual(expected, actual)

    def test_zcorr_1(self):
        input_x = [1, 2, 3]
        input_y = [7, 8, 9]
        expected = 1.0
        actual = formulas.zcorr(input_x, input_y)
        self.assertEqual(expected, actual)

    def test_zcorr_2(self):
        input_x = [1, 2, 3]
        input_y = [3, 2, 1]
        expected = -1.0
        actual = formulas.zcorr(input_x, input_y)
        self.assertEqual(expected, actual)