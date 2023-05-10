from utils import *

A = [[84, 0, 0, 0, 0, 0, 0, 0], [115, 70, 0, 0, 0, 0, 0, 0], [14, 28, 43, 0, 0, 0, 0, 0], [97, 21, 6, 12, 0, 0, 0, 0], [96, 43, 2, 104, 112, 0, 0, 0], [18, 49, 31, 47, 111, 11, 0, 0], [11, 120, 20, 101, 30, 93, 27, 0], [70, 12, 95, 24, 10, 73, 29, 38]]

e = [19, 118, 40, 76, 89, 46, 21, 15]
def MatrixMult(A, v):
    res = [0 for i in range(8)]
    
    for i in range(8):
        for(j) in range(8):
            res[i] = Add(res[i], Multiply(v[j], A[i][j]))
    # print(res)
    return res

# A is 8 x 8 matrix, e is 1x8 vector, plaintext is also same as e
def EAEAE(A, e, plaintext):
    c = plaintext.copy()
    # print("e=", e)
    c = [exp(c[i], ele) for i, ele in enumerate(e)]
    c = MatrixMult(A, c)
    c = [exp(c[i], ele) for i, ele in enumerate(e)]
    c = MatrixMult(A, c)
    c = [exp(c[i], ele) for i, ele in enumerate(e)]
    # print("c=" , c)
    return c


password = 'gsgqljiilnlimsmoiklfgnhsmfgomliu'

pass_bin = ''
for ele in password:
    pass_bin += mapping[ele]

pass_bin1 = pass_bin[:len(pass_bin)//2]
pass_bin2 = pass_bin[len(pass_bin)//2:]

print(len(pass_bin1), len(pass_bin2))

def get_plaintext(passwrd):


    plain1 = [0 for i in range(8)]

    for i in range(8):
        t = int(passwrd[i*8:i*8+8], 2)
        print(t)
        for j in range(128):
            plain1[i] = j
            res = EAEAE(A, e, plain1)
            if res[i] == t:
                break

    return plain1

plain1 = get_plaintext(pass_bin1)
plain2 = get_plaintext(pass_bin2)

print(plain1, plain2)


