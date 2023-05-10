from utils import *

A = [[84, 0, 0, 0, 0, 0, 0, 0], [115, 70, 0, 0, 0, 0, 0, 0], [0, 28, 43, 0, 0, 0, 0, 0], [0, 0, 6, 12, 0, 0, 0, 0], [0, 0, 0, 104, 112, 0, 0, 0], [0, 0, 0, 0, 111, 11, 0, 0], [0, 0, 0, 0, 0, 93, 27, 0], [0, 0, 0, 0, 0, 0, 29, 38]]

e = [19, 118, 40, 76, 89, 46, 21, 15]

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


AA = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        AA[i][j] = A[i][j]
# AA[0][0] = 0
print(A)

for i in range(2, 8):
    
    # print(off)
    for j in range(0, 8-i):
        print(j, j+i)
        plains = [p[(j)*2:(j)*2+2] for p in plaintexts[127*(j) : 127*(j) + 127]]
        ciphers = [p[(j+i)*2:(j+i)*2+2] for p in ciphertexts[127*(j) : 127*(j) + 127]]
        # print(plains[0], ciphers[0])
        plain_vals = [conv_to_num(p) for p in plains]
        cipher_vals = [conv_to_num(p) for p in ciphers]
        for p in range(8):
            for q in range(8):
                AA[p][q] = A[p][q]
        for m in range(128):

            AA[i+j][j] = m 
            flag = 1

            for n in range(127):
                v = [0 for i in range(8)]
                v[j] = plain_vals[n]
                res = EAEAE(AA, e, v)
                if res[j+i] != cipher_vals[n]:
                    flag = 0
                    break

            if flag == 1:
                # print(j+off, j)
                if A[j+i][j] == 0:
                    A[j+i][j] = m
                    # print("hey")
                else:
                    print(A[j+i][j])
                    print("repeat")
                

print(A)