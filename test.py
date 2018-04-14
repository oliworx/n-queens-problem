import unittest
import n_queens


class NQueensTest(unittest.TestCase):

    def testNumSolutions(self):
        self.assertEqual(n_queens.run(14), 365596)

    def testSolutionsForFirstQueen(self):
        self.assertEqual(n_queens.run_first_queen(0), 11892)
        self.assertEqual(n_queens.run_first_queen(1), 16488)
        self.assertEqual(n_queens.run_first_queen(2), 23024)
        self.assertEqual(n_queens.run_first_queen(3), 27494)
        self.assertEqual(n_queens.run_first_queen(4), 32163)
        self.assertEqual(n_queens.run_first_queen(5), 34760)
        self.assertEqual(n_queens.run_first_queen(6), 36977)


if __name__ == "__main__":
    unittest.main()
