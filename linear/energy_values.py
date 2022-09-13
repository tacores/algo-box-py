# python3

EPS = 1e-6
PRECISION = 20

"""
ガウスの消去法（Gauss Elimination）で
N x N の連立方程式を解く。
解は必ずあるものとする。
"""

def ReadEquation():
    size = int(input())
    a = [[] for _ in range(size)]
    for row in range(size):
        line = list(map(float, input().split()))
        a[row] = line
    return a

def printEquation(a):
    print('********************')
    for i in range(len(a)):
        print(a[i])
    print('********************')

def SolveEquation(a):
    size = len(a)
    rows = size
    vals = size

    for pivot in range(rows):

        #printEquation(a)
        # ピボット行のピボット列が0以外になるように行を入れ替える
        for r in range(pivot, rows):
            if a[r][pivot] != 0:
                if r == pivot:
                    break
                a[pivot], a[r] = a[r], a[pivot]
                break
        
        # ピボットの係数を１にスケールする
        scale = a[pivot][pivot]
        for n in range(vals + 1):
            a[pivot][n] /= scale

        # ピボット行を加減算して、ピボット行以外の行から変数を1つ消す
        for r in range(rows):
            if r != pivot:
                scale = a[r][pivot]
                for n in range(vals + 1):
                    a[r][n] -= a[pivot][n] * scale
        #printEquation(a)
    
    result = []
    for v in range(vals):
        result.append(a[v][vals])
    return result

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
