import unittest
import algorithms


#Test quick sort
class TestQuickSort(unittest.TestCase):
    arr = [10,7,8,9,1,5]
    n = len(arr) - 1
    target_arr = [1,5,7,8,9,10]

    def test_sort(self):
        algorithms.quick_sort(self.arr, 0, self.n)
        self.assertEqual(self.arr, self.target_arr, "Arrays do not match")


if __name__ == '__main__':
    unittest.main()

