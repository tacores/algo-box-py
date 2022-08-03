# python3
import sys

# BWTから元の文字列を復元する
def InverseBWT(bwt):

    L = len(bwt)
    FirstColumn = sorted(bwt)
    LastColumn = bwt

    ith_of_the_char_l = ['' for i in range(L)]
    pos_of_the_ith_char_f = {}
    char_cnt_l = {}
    char_cnt_f = {}

    for i in range(L):
        # LastColumnで、その位置の文字が何番目の出現かを持っておく
        c = LastColumn[i]
        if c not in char_cnt_l:
            char_cnt_l[c] = 0
        char_cnt_l[c] += 1
        ith_of_the_char_l[i] = c + str(char_cnt_l[c]) # G1 A3 etc
    
        # i番目の文字Xの位置をマップで持っておく
        c = FirstColumn[i]
        if c not in char_cnt_f:
            char_cnt_f[c] = 0
        char_cnt_f[c] += 1
        pos_of_the_ith_char_f[c + str(char_cnt_f[c])] = i

    assert(FirstColumn[0] == '$')
    result = '$'
    pos_l = 0
    while len(result) < L:
        char_ith = ith_of_the_char_l[pos_l]
        result += char_ith[0]   # result = char_ith[0] + result より速い
        pos_l = pos_of_the_ith_char_f[char_ith]
    
    return result[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))