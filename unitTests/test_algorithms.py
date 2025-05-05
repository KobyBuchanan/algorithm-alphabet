import unittest
import algorithms

#To run tests
#./test.sh

#Test quick sort
class TestQuickSort(unittest.TestCase):
    arr = [10,7,8,9,1,5]
    n = len(arr) - 1
    target_arr = [1,5,7,8,9,10]

    def test_sort(self):
        algorithms.quick_sort(self.arr, 0, self.n)
        self.assertEqual(self.arr, self.target_arr, "Arrays do not match")


#Test nQueens
class TestnQueens(unittest.TestCase):
    def testKnownSolutions(self):
        n = 4
        target_solution = [[2,4,1,3],[3,1,4,2]]
        solution = algorithms.nQueen(n)
        self.assertEqual(solution,target_solution,"Answers do not match")

    def testKnownNoSolutions(self):
        n = 2
        target_solution = "There are no solutions for this value of n"
        solution = algorithms.nQueen(n)
        self.assertEqual(solution,target_solution,"Answers do not match")


if __name__ == '__main__':
    unittest.main()

