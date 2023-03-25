import re
f = open('out.txt')
word_list = f.read().split('\n')

f.close()

# print(word_list)


inverse_mapping = {
    'f' : '0',
    'g' : '1' ,
    'h' : '2',
    'i' : '3',
    'j' : '4',
    'k' : '5',
    'l' : '6',
    'm' : '7',
    'n' : '8',
    'o' : '9',
    'p' : 'a',
    'q' : 'b',
    'r' : 'c',
    's' : 'd',
    't' : 'e',
    'u' : 'f',
}

inv_final_permuatation = [
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,

]

expansion_permutation = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
]

inv_PBox_perm = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]




num_bits = 32

def invert_final_perm(l):
    t = ''
    for i, ele in enumerate(l):
        t = t + str(l[inv_final_permuatation[i]-1])
    return t

def invert_PBox_perm(l):
    t = ''
    #print(len(l))
    for i, ele in enumerate(l):
        t = t + str(l[inv_PBox_perm[i]-1])
    return t

def apply_expansion(l):
    t = ''
    for i, ele in enumerate(expansion_permutation):
        t = t + str(l[ele-1])
    return t


lines1 = []
lines2 = []
lines3 = []

outputs = []
for i in range(len(word_list)):
    t = ''
    for j in range(len(word_list[i])):
        t += inverse_mapping[word_list[i][j]]
    t = bin(int(t, 16))[2:].zfill(num_bits * 2)
    if i ==0:
        print(t)
    t = invert_final_perm(t)
    outputs.append(t)

print(outputs[0])


    

leftXor = '04000000'

for i in range(0, len(outputs), 2):
    # inverse the final permutation in the right half
    l6 = bin(int(outputs[i][:32], 2) ^ int(outputs[i+1][:32], 2))[2:].zfill(num_bits)
    r6 = int(outputs[i][32:], 2) ^ int(outputs[i+1][32:], 2)
    # print(r6)
    r6 = bin(r6 ^ int(leftXor, 16))[2:].zfill(32)
    r6 = invert_PBox_perm(r6)
    r5 = l6
    # left half of 6th round is same as right half of 5th round
    # applying expansion step 
    ExpR5 = apply_expansion(r5)
    lines1.append(ExpR5)
    lines2.append(r6)
    lines3.append(apply_expansion(outputs[i][:32]))
    # lines3.append(apply_expansion(outputs[i+1][32:]))

f1 = open('SBoxInputXor.txt', 'w')
for ele in lines1:
    f1.write(ele + '\n')
f1.close()

f2 = open('SBoxOutputXor.txt', 'w')
for ele in lines2:
    f2.write(ele + '\n')
f2.close()

f3 = open('Expansions.txt','w')
for ele in lines3:
    f3.write(ele + '\n')
f3.close()


    



        

