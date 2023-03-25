# using the 4 round characteristic (405c0000, 04000000) -> (00540000, 04000000) 
# 

import random


N = 100000
mapping = {
    '0': 'f',
    '1': 'g',
    '2': 'h',
    '3': 'i',
    '4': 'j',
    '5': 'k',
    '6': 'l',
    '7': 'm',
    '8': 'n',
    '9': 'o',
    'a': 'p',
    'b': 'q',
    'c': 'r',
    'd': 's',
    'e': 't',
    'f': 'u',
}


inputXorLeft = '405c0000'
inputXorRight = '04000000'

inputXor = inputXorLeft + inputXorRight
scale = 16
num_bits = 64

# as taken from Bruce Schnieder Applied Cryptography
inv_init_permutation = [ 
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25,

]

# inverting the initial permuatation
temp = ''
input = bin(int(inputXor, scale))[2:].zfill(num_bits)
input= str(input)

for i, ele in enumerate(input):
    temp = temp + str(input[inv_init_permutation[i]-1])
print(input)

inputXor = hex(int(temp, 2))[2:].zfill(16)
# print(inputXor)



plaintexts = []

# generate plaintexts in binary form
for i in range(N):
    currPlaintext = ['', '']
    for j in inputXor:
        ch1 = random.choice([k for k in range(16)])
        ch2 = ch1 ^ int(j, 16) 
        currPlaintext[0] += str(hex(ch1)[2:])
        currPlaintext[1] += str(hex(ch2)[2:])
   
    plaintexts.append(currPlaintext[0])
    plaintexts.append(currPlaintext[1])

plaintexts_txt = []

for i in range(len(plaintexts)):
    x= ''
    for j in range(len(plaintexts[i])):
        
        x = x + mapping[plaintexts[i][j]]
    plaintexts_txt.append(x)
            
# print(plaintexts)
with open('plaintexts.txt', 'w') as f:
    for p in plaintexts_txt:
        f.write(p)
        f.write('\n')





