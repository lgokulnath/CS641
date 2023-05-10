# #Run this file to get the possible values for the diagonal elements of the key matrix and all elements of the exponentiation vector

# N = 128

# mapping = {'f': '0000', 'g': '0001', 'h': '0010', 'i': '0011', 'j': '0100', 'k': '0101', 'l': '0110', 'm': '0111',
#     'n': '1000', 'o': '1001', 'p': '1010', 'q': '1011', 'r': '1100', 's': '1101', 't': '1110', 'u': '1111'}

# inverse_mapping = {}

# for key in list(mapping.keys()):
#     inverse_mapping[mapping[key]] = key

# IRREDUCIBLE_POL = [1, 0, 0, 0, 0, 0, 1, 1]
# mult_cache = [[-1]*128 for i in range(128)]
# expo_cache = [[-1]*128 for i in range(128)]

# # binary exponentiation
# def exponent(num, power):
#     num %= N
#     ans = 1
#     while power > 0:
#         if power & 1 :
#             ans = (ans * num) % N
#         num = (num * num) % N 
#         power = power >> 1
#     return ans


def conv_to_num(block):
    fir = mapping[block[0]]
    sec = mapping[block[1]]
    return 16*int(fir, 2) + int(sec, 2)


file = open("plaintexts.txt", "r")
plaintexts = file.readlines()
file.close()

file = open("out.txt", "r")
ciphertexts = file.readlines()
file.close()

possible = [[]*8]*8

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# # print(len(possibleai))

# GF128_MSB = 1<<6
# GF128_MASK = (1<<7) - 1

# def Add (elem1, elem2):
#     elem1 = int(elem1)
#     elem2 = int(elem2)
#     return elem1 ^ elem2

# def Multiply (elem1, elem2):
#     if mult_cache[elem1][elem2] != -1:
#         return mult_cache[elem1][elem2]

#     elem1 = int(elem1)
#     elem2 = int(elem2)
#     elem3 = 0
#     ind = 0
#     for ind in range(7):
#         elem3 <<= 1
#         if (elem1 & GF128_MSB) :
#             elem3 = Add(elem3, elem2)

#         elem1 <<= 1
#     upper = elem3 >> 7
#     product = Add(Add(upper, upper<<1), elem3 & GF128_MASK)

#     mult_cache[elem1>>7][elem2] = product
#     mult_cache[elem2][elem1>>7] = product
#     return product

# def Exponentiate (elem, power):
#     if expo_cache[elem][power] != -1:
#         return expo_cache[elem][power]

#     result = 0
#     if power == 0:
#         result = 1
#     elif power == 1:
#         result = elem
#     elif power%2 == 0:
#         sqrt_elem = Exponentiate(elem, power>>1)
#         result = Multiply(sqrt_elem, sqrt_elem)
#     else:
#         sqrt_elem = Exponentiate(elem, power>>1)
#         result = Multiply(sqrt_elem, sqrt_elem)
#         result = Multiply(elem, result)

#     expo_cache[elem][power] = result
#     return result

# def encrypt_block(block, ai, ei):
#     expo = Exponentiate(block, ei)
#     mult = Multiply(expo, ai)
#     expo = Exponentiate(mult, ei)
#     mult = Multiply(expo, ai)
#     expo = Exponentiate(mult, ei)
#     return expo

# cnt=0

# for i in range(8):
#     plains = plaintexts[127*i:127*i+127]
#     ciphers = ciphertexts[127*i:127*i+127]
#     for (plain, cipher) in zip(plains, ciphers):
#         temp = []
#         block_plain = plain[2*i:2*i+2]
#         block_cipher = cipher[2*i:2*i+2]

#         # get binary values 
#         blockval_plain = conv_to_num(block_plain)
#         blockval_cipher = conv_to_num(block_cipher)
#         for ai in range(128):
#             for ei in range(1, 127):
#                 encrypted_blockval_plain = encrypt_block(blockval_plain, ai, ei)
#                 if blockval_cipher == encrypted_blockval_plain:
#                     if [ai,ei] not in temp:
#                         temp.append([ai, ei])

#         if len(possible[i])==0:
#             possible[i] = temp
#         else:
#             possible[i] = intersection(possible[i], temp)
#         cnt+=1
#     print("Done for block",i)
#     print("The possible list is now", possible)

# print(possible)

from utils import *

N = 128

mapping = {'f': '0000', 'g': '0001', 'h': '0010', 'i': '0011', 'j': '0100', 'k': '0101', 'l': '0110', 'm': '0111',
    'n': '1000', 'o': '1001', 'p': '1010', 'q': '1011', 'r': '1100', 's': '1101', 't': '1110', 'u': '1111'}

inverse_mapping = {}

for key in list(mapping.keys()):
    inverse_mapping[mapping[key]] = key

def encrypt_block(v, a, e):
    v = exp(v, e)
    v = Multiply(v, a)
    v = exp(v, e)
    v = Multiply(v, a)
    v = exp(v, e)
    return v

cnt=0

for i in range(8):
    plains = plaintexts[127*i:127*i+127]
    ciphers = ciphertexts[127*i:127*i+127]
    for (plain, cipher) in zip(plains, ciphers):
        temp = []
        block_plain = plain[2*i:2*i+2]
        block_cipher = cipher[2*i:2*i+2]

        # get binary values 
        blockval_plain = conv_to_num(block_plain)
        blockval_cipher = conv_to_num(block_cipher)
        for ai in range(128):
            for ei in range(1, 127):
                encrypted_blockval_plain = encrypt_block(blockval_plain, ai, ei)
                if blockval_cipher == encrypted_blockval_plain:
                    if [ai,ei] not in temp:
                        temp.append([ai, ei])

        if len(possible[i])==0:
            possible[i] = temp
        else:
            possible[i] = intersection(possible[i], temp)
        cnt+=1
    print("Done for block",i)
    print("The possible list is now", possible)




