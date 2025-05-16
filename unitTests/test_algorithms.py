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


class Test_aStar(unittest.TestCase):
    def testGrid(self):
        target_grid_string = "[05][19][05][18]\n[01][19][15][04]\n[05][02][15][20]\n[18][20][15][16]\n"
        width,height = 4,4
        grid = algorithms.TrafficGrid(width,height)
        self.assertEqual(repr(grid),target_grid_string,"Answers do not match")

    def testGridBarriers(self):
        target_grid_string = "[05][19][05][999]\n[01][999][999][04]\n[05][02][999][20]\n[18][20][15][999]\n"
        width,height = 4,4
        grid = algorithms.TrafficGrid(width,height,allow_barriers=True)
        self.assertEqual(repr(grid),target_grid_string,"Answers do not match")
    
    def testSearchNoBarriers(self):
        target_path = [(0,0),(0,1),(1,1),(2,1),(2,2)]
        width,height = 3,3
        src = algorithms.Tile(0,0)
        dest = algorithms.Tile(2,2)
        grid = algorithms.TrafficGrid(width,height)
        path = algorithms.a_star_search(grid, src, dest)
        self.assertEqual(path,target_path,"Answers do not match")

    def testSearchBarriers(self):
        target_path = "No path exists from chosen source to destination"
        width,height = 3,3
        src = algorithms.Tile(0,0)
        dest = algorithms.Tile(2,2)
        grid = algorithms.TrafficGrid(width,height,allow_barriers=True)
        path = algorithms.a_star_search(grid, src, dest)
        self.assertEqual(path,target_path,"Answers do not match")


if __name__ == '__main__':
    unittest.main()

