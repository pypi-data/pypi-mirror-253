import unittest
from .tex_processing import solution_to_tikz, solution_to_align

class TestTexProcessing(unittest.TestCase):
    def test_solution_to_tikz(self):
        # Test case 1: Valid solution file and TikZ picture file
        file_sol = "test_solution.tex"
        file_tikz = "test_tikzpicture.tex"
        expected_output = "picture/main.png"
        self.assertEqual(solution_to_tikz(file_sol, file_tikz), expected_output)

        # Test case 2: Valid solution file but TikZ picture file not found
        file_sol = "test_solution.tex"
        file_tikz = "nonexistent_tikzpicture.tex"
        with self.assertRaises(FileNotFoundError):
            solution_to_tikz(file_sol, file_tikz)

        # Test case 3: Solution file not found
        file_sol = "nonexistent_solution.tex"
        file_tikz = "test_tikzpicture.tex"
        with self.assertRaises(FileNotFoundError):
            solution_to_tikz(file_sol, file_tikz)

    def test_solution_to_align(self):
        # Test case 1: Valid solution file with align equations
        file_sol = "test_solution.tex"
        expected_output = {
            'set_1': [
                '\\intertext{Equation 1}',
                'x = y + z',
                'a = b + c'
            ],
            'set_2': [
                '\\intertext{Equation 2}',
                'p = q + r',
                'm = n + o'
            ]
        }
        self.assertEqual(solution_to_align(file_sol), expected_output)

        # Test case 2: Valid solution file without align equations
        file_sol = "test_solution_without_align.tex"
        expected_output = {}
        self.assertEqual(solution_to_align(file_sol), expected_output)

        # Test case 3: Solution file not found
        file_sol = "nonexistent_solution.tex"
        with self.assertRaises(FileNotFoundError):
            solution_to_align(file_sol)

if __name__ == '__main__':
    unittest.main()