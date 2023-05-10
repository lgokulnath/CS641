
from utils import *
import numpy as np

#calculated from get_diagonals.py
possible = [[[27, 1], [84, 19], [84, 107]], [[70, 118], [72, 53], [101, 83]], [[14, 89], [43, 40], [72, 125]], [[12, 76], [38, 4], [113, 47]], [[20, 125], [112, 89], [118, 40]], [[11, 46], [71, 96], [125, 112]], [[27, 21], [63, 88], [123, 18]], [[38, 15], [61, 31], [125, 81]]]

file = open("plaintexts.txt", "r")
plaintexts = file.readlines()
file.close()

file = open("out.txt", "r")
ciphertexts = file.readlines()
file.close()



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


    


# obtaining the complete matrix
A = [[0 for i in range(8)] for j in range(8)]
AA = [[0 for i in range(8)] for j in range(8)]
e = [0 for i in range(8)]
ee = [0 for i in range(8)]



for i in range(7):
    j = i+1
    print(j)
    a_p = [ele[0] for ele in possible[j]]
    e_p = [ele[1] for ele in possible[j]]
    # print(a_p)
    a_prev = [ele[0] for ele in possible[j-1]]
    e_prev = [ele[1] for ele in possible[j-1]]
    plains = [p[(j-1)*2:(j-1)*2+2] for p in plaintexts[127*(j-1) : 127*(j-1) + 127]]
    ciphers = [p[(j)*2:(j)*2+2] for p in ciphertexts[127*(j-1) : 127*(j-1) + 127]]
    # print(plains[0], ciphers[0])
    plain_vals = [conv_to_num(p) for p in plains]
    cipher_vals = [conv_to_num(p) for p in ciphers]
    # print(plain_vals)
    flag = 1
    for k in range(len(a_p)):
       
        for l in range(len(a_prev)):
            
            for m in range(128):
                flag = 1
                A[j][j] = a_p[k]
                A[j-1][j-1] = a_prev[l]
                A[j][j-1] = m 
                e[j] = e_p[k]
                # print("e[j] = ", e[j])
                e[j-1] = e_prev[l] 
                v = [0 for i in range(8)]
                for n in range(1, 128):
                    
                    v[j-1] = plain_vals[n-1]
                    # print(A, e)
                    # print(v)
                    res = EAEAE(A, e, v)
                    # print(res[j], cipher_vals[n-1], m)
                    # exp(Add(Multiply(exp(Multiply(exp(v[j-1], e[j-1]), a_prev[l]), e[j-1]), j), Multiply(exp(Multiply(exp(x, exp2), j), exp1), diag1)), exp1)
                    if res[j]!= cipher_vals[n-1]:
                        # print(k, l, m, n)
                        flag = 0
                        break
                
                if flag == 1:
                    
                    print(a_p[k], a_prev[l], e_p[k], e_prev[l],  m)
                    AA[j][j] = a_p[k]
                    AA[j-1][j-1] = a_prev[l]
                    AA[j][j-1] = m
                    ee[j] = e_p[k]
                    ee[j-1] = e_prev[l]

print(AA)
print(ee)                


                    


                
