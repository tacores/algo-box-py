# python3

import unittest
from puzzle_5x5 import Square
from puzzle_5x5 import solve

class w2_1_test(unittest.TestCase):

    def test_solve_sample1(self):
        squares = []
        squares.append(Square('black', 'black', 'green', 'red')) #0
        squares.append(Square('black', 'red', 'green', 'blue')) #1
        squares.append(Square('black', 'blue', 'blue', 'red')) #2
        squares.append(Square('black', 'red', 'green', 'green')) #3
        squares.append(Square('black', 'green', 'red', 'black')) #4
        squares.append(Square('green', 'black', 'red', 'red')) #5
        squares.append(Square('green', 'red', 'blue', 'green')) #6
        squares.append(Square('blue', 'green', 'red', 'blue')) #7
        squares.append(Square('green', 'blue', 'blue', 'red')) #8
        squares.append(Square('red', 'red', 'green', 'black')) #9
        squares.append(Square('red', 'black', 'red', 'blue')) #10
        squares.append(Square('blue', 'blue', 'green', 'blue')) #11
        squares.append(Square('red', 'blue', 'green', 'green')) #12
        squares.append(Square('blue', 'green', 'red', 'blue')) #13
        squares.append(Square('green', 'blue', 'blue', 'black')) #14
        squares.append(Square('red', 'black', 'green', 'red')) #15
        squares.append(Square('green', 'red', 'blue', 'red')) #16
        squares.append(Square('green', 'red', 'blue', 'red')) #17
        squares.append(Square('red', 'red', 'blue', 'green')) #18
        squares.append(Square('blue', 'green', 'red', 'black')) #19
        squares.append(Square('green', 'black', 'black', 'red')) #20
        squares.append(Square('blue', 'red', 'black', 'green')) #21
        squares.append(Square('blue', 'green', 'black', 'green')) #22
        squares.append(Square('blue', 'green', 'black', 'red')) #23
        squares.append(Square('red', 'red', 'black', 'black')) #24

        expected = [
            "(black,black,green,red);(black,red,green,blue);(black,blue,blue,red);(black,red,green,green);(black,green,red,black)",
            "(green,black,red,red);(green,red,blue,green);(blue,green,red,blue);(green,blue,blue,red);(red,red,green,black)",
            "(red,black,red,blue);(blue,blue,green,blue);(red,blue,green,green);(blue,green,red,blue);(green,blue,blue,black)",
            "(red,black,green,red);(green,red,blue,red);(green,red,blue,red);(red,red,blue,green);(blue,green,red,black)",
            "(green,black,black,red);(blue,red,black,green);(blue,green,black,green);(blue,green,black,red);(red,red,black,black)"
        ]
        self.assertEqual(solve(squares), expected)


    def test_solve_sample1_reverse(self):
        squares = []
        squares.append(Square('black', 'black', 'green', 'red')) #0
        squares.append(Square('black', 'red', 'green', 'blue')) #1
        squares.append(Square('black', 'blue', 'blue', 'red')) #2
        squares.append(Square('black', 'red', 'green', 'green')) #3
        squares.append(Square('black', 'green', 'red', 'black')) #4
        squares.append(Square('green', 'black', 'red', 'red')) #5
        squares.append(Square('green', 'red', 'blue', 'green')) #6
        squares.append(Square('blue', 'green', 'red', 'blue')) #7
        squares.append(Square('green', 'blue', 'blue', 'red')) #8
        squares.append(Square('red', 'red', 'green', 'black')) #9
        squares.append(Square('red', 'black', 'red', 'blue')) #10
        squares.append(Square('blue', 'blue', 'green', 'blue')) #11
        squares.append(Square('red', 'blue', 'green', 'green')) #12
        squares.append(Square('blue', 'green', 'red', 'blue')) #13
        squares.append(Square('green', 'blue', 'blue', 'black')) #14
        squares.append(Square('red', 'black', 'green', 'red')) #15
        squares.append(Square('green', 'red', 'blue', 'red')) #16
        squares.append(Square('green', 'red', 'blue', 'red')) #17
        squares.append(Square('red', 'red', 'blue', 'green')) #18
        squares.append(Square('blue', 'green', 'red', 'black')) #19
        squares.append(Square('green', 'black', 'black', 'red')) #20
        squares.append(Square('blue', 'red', 'black', 'green')) #21
        squares.append(Square('blue', 'green', 'black', 'green')) #22
        squares.append(Square('blue', 'green', 'black', 'red')) #23
        squares.append(Square('red', 'red', 'black', 'black')) #24
        squares.reverse()   # reverse

        expected = [
            "(black,black,green,red);(black,red,green,blue);(black,blue,blue,red);(black,red,green,green);(black,green,red,black)",
            "(green,black,red,red);(green,red,blue,green);(blue,green,red,blue);(green,blue,blue,red);(red,red,green,black)",
            "(red,black,red,blue);(blue,blue,green,blue);(red,blue,green,green);(blue,green,red,blue);(green,blue,blue,black)",
            "(red,black,green,red);(green,red,blue,red);(green,red,blue,red);(red,red,blue,green);(blue,green,red,black)",
            "(green,black,black,red);(blue,red,black,green);(blue,green,black,green);(blue,green,black,red);(red,red,black,black)"
        ]
        self.assertEqual(solve(squares), expected)


if __name__ == '__main__':
    unittest.main()


