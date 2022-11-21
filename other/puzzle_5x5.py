# python3

import itertools

"""
5×5の正方形パネルを並べるパズルを解く。
(top, left, bottom, right) の形で25枚の四角形が与えられる。
詳細は、puzzle_5x5.xlsx 参照。

特にこれといったアルゴリズムやテクニックは使っていない。
外枠が黒色であることを利用して、まず四隅のパネルを確定し、
四辺の組み合わせを総当たりに近い形で調べている。
"""

class Square:
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.row = -1
        self.column = -1
    
    def __str__(self):
        return "(" + self.top + "," + self.left + "," + self.bottom + "," + self.right + ")"

def solve(squares):
    n = len(squares)
    top_left = top_right = bottom_left = bottom_right = -1
    tops = []
    lefts = []
    rights = []
    bottoms = []
    centers = []
    result = [0] * 25

    for i in range(n):
        s = squares[i]
        if s.top == 'black' and s.left == 'black':
            top_left = i
        elif s.top == 'black' and s.right == 'black':
            top_right = i
        elif s.top == 'black':
            tops.append(i)
        elif s.bottom == 'black' and s.left == 'black':
            bottom_left = i
        elif s.bottom == 'black' and s.right == 'black':
            bottom_right = i
        elif s.bottom == 'black':
            bottoms.append(i)
        elif s.left == 'black':
            lefts.append(i)
        elif s.right == 'black':
            rights.append(i)
        else:
            centers.append(i)

    for top_p in itertools.permutations(tops):
        if squares[top_left].right != squares[top_p[0]].left \
            or squares[top_p[0]].right != squares[top_p[1]].left \
            or squares[top_p[1]].right != squares[top_p[2]].left \
            or squares[top_p[2]].right != squares[top_right].left:
            continue
        for bottom_p in itertools.permutations(bottoms):
            if squares[bottom_left].right != squares[bottom_p[0]].left \
                or squares[bottom_p[0]].right != squares[bottom_p[1]].left \
                or squares[bottom_p[1]].right != squares[bottom_p[2]].left \
                or squares[bottom_p[2]].right != squares[bottom_right].left:
                continue
            for left_p in itertools.permutations(lefts):
                if squares[top_left].bottom != squares[left_p[0]].top \
                    or squares[left_p[0]].bottom != squares[left_p[1]].top \
                    or squares[left_p[1]].bottom != squares[left_p[2]].top \
                    or squares[left_p[2]].bottom != squares[bottom_left].top:
                    continue
                for right_p in itertools.permutations(rights):
                    if squares[top_right].bottom != squares[right_p[0]].top \
                        or squares[right_p[0]].bottom != squares[right_p[1]].top \
                        or squares[right_p[1]].bottom != squares[right_p[2]].top \
                        or squares[right_p[2]].bottom != squares[bottom_right].top:
                        continue
                    for center_p in itertools.permutations(centers):
                        if squares[top_p[0]].bottom != squares[center_p[0]].top \
                            or squares[top_p[1]].bottom != squares[center_p[1]].top \
                            or squares[top_p[2]].bottom != squares[center_p[2]].top \
                            or squares[left_p[0]].right != squares[center_p[0]].left \
                            or squares[left_p[1]].right != squares[center_p[3]].left \
                            or squares[left_p[2]].right != squares[center_p[6]].left \
                            or squares[right_p[0]].left != squares[center_p[2]].right \
                            or squares[right_p[1]].left != squares[center_p[5]].right \
                            or squares[right_p[2]].left != squares[center_p[8]].right \
                            or squares[bottom_p[0]].top != squares[center_p[6]].bottom \
                            or squares[bottom_p[1]].top != squares[center_p[7]].bottom \
                            or squares[bottom_p[2]].top != squares[center_p[8]].bottom \
                            or squares[center_p[0]].right != squares[center_p[1]].left \
                            or squares[center_p[1]].right != squares[center_p[2]].left \
                            or squares[center_p[3]].right != squares[center_p[4]].left \
                            or squares[center_p[4]].right != squares[center_p[5]].left \
                            or squares[center_p[6]].right != squares[center_p[7]].left \
                            or squares[center_p[7]].right != squares[center_p[8]].left \
                            or squares[center_p[0]].bottom != squares[center_p[3]].top \
                            or squares[center_p[3]].bottom != squares[center_p[6]].top \
                            or squares[center_p[1]].bottom != squares[center_p[4]].top \
                            or squares[center_p[4]].bottom != squares[center_p[7]].top \
                            or squares[center_p[2]].bottom != squares[center_p[5]].top \
                            or squares[center_p[5]].bottom != squares[center_p[8]].top:
                            continue
                        
                        # solved!
                        result[0] = top_left
                        result[1] = top_p[0]
                        result[2] = top_p[1]
                        result[3] = top_p[2]
                        result[4] = top_right
                        result[5] = left_p[0]
                        result[6] = center_p[0]
                        result[7] = center_p[1]
                        result[8] = center_p[2]
                        result[9] = right_p[0]
                        result[10] = left_p[1]
                        result[11] = center_p[3]
                        result[12] = center_p[4]
                        result[13] = center_p[5]
                        result[14] = right_p[1]
                        result[15] = left_p[2]
                        result[16] = center_p[6]
                        result[17] = center_p[7]
                        result[18] = center_p[8]
                        result[19] = right_p[2]
                        result[20] = bottom_left
                        result[21] = bottom_p[0]
                        result[22] = bottom_p[1]
                        result[23] = bottom_p[2]
                        result[24] = bottom_right

                        ret = []
                        for i in range(5):
                            n = i * 5
                            s = ""
                            for j in range(5):
                                if j != 0:
                                    s += ";"
                                s += str(squares[result[n + j]])
                            ret.append(s)
                        return ret


def read_data():
    squares = []
    for i in range(25):
        line = input()[1:-1]
        (top, left, bottom, right) = line.split(',')
        squares.append(Square(top, left, bottom, right))
    return squares

if __name__ == '__main__':
    squares = read_data()
    result = solve(squares)
    for s in result:
        print(s)
