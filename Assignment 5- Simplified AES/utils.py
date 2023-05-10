from pyfinite import ffield

N = 128

mapping = {'f': '0000', 'g': '0001', 'h': '0010', 'i': '0011', 'j': '0100', 'k': '0101', 'l': '0110', 'm': '0111',
    'n': '1000', 'o': '1001', 'p': '1010', 'q': '1011', 'r': '1100', 's': '1101', 't': '1110', 'u': '1111'}

inverse_mapping = {}

for key in list(mapping.keys()):
    inverse_mapping[mapping[key]] = key

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

F = ffield.FField(7)

def Add(a, b):
    return a ^ b

def Multiply(a, b):
    return F.Multiply(a, b)

def exp(a, n):
    if n == 0 :
        if a != 0:
            return 1
        else:
            return 0
    if n == 1:
        return a
    if n % 2 == 0:
        t = exp(a, n/2)
        return Multiply(t, t)
    else:
        t = exp(a, n // 2)
        return Multiply(Multiply(t, t), a)
    
def encrypt(v, a, e):
    v = exp(v, e)
    v = Multiply(v, a)
    v = exp(v, e)
    v = Multiply(v, a)
    v = exp(v, e)
    return v

