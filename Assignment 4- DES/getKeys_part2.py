key_map = [
    [24, 27, 21, 6, 11, 15 ,],
    [13, 10, 25, 16, 3, 20, ],
    [5, 1, 22, 14, 8, 18, ],
    [26, 17, 9, 2, 23, 12, ],
    [51, 34, 41, 47, 29, 37,],
    [40, 50, 33, 55, 43, 30, ],
    [54, 31, 49, 38, 44, 35, ],
    [56, 52, 32, 46, 39, 42, ],
]

disc_keys = [1, 2, 5, 6, 7, 8]
keys = [61, 51, -1, -1, 27, 54, 5, 52]

key_size = 56

key = ['_' for i in range(key_size)]


for i in disc_keys:
    for j in range(6):
        # print(key_map[i-1][j], i-1)
        key[key_map[i-1][j]-1] = (keys[i-1] >> (6-j-1)) & 1

print(key)



possible_keys = []

for i in range(2**20):
    t = key.copy()
    cnt = 19
    # print(t)
    s = ''
    for j in range(56):
       
        if t[j] == '_':
            t[j] = (i >> cnt) & 1
            cnt -= 1
        s += str(t[j])
    # print(cnt)

    possible_keys.append(s)

with open('poss_keys.txt', 'w') as f:
    for i in range(len(possible_keys)):
        f.write(possible_keys[i])
        f.write('\n')

# print(possible_keys[:2])

# if(possible_keys[0] == possible_keys[1]):
#     print("wrong")