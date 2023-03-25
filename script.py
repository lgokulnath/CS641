import string


# Team name


print("bletchley_hut_8")

# Password
print("bletchley279")

print("4")

print("read")

c = 0

f = open('plaintexts.txt', 'r')


plaintexts = f.readlines()

f.close()

for p in plaintexts:
    if p != '\n':
        print(p)
        print('c')

print('back')
print('quit')


# count = 1
# chrw = ""

# import re
# word_list = list()
# with open('out.txt') as f:
#     for line in f.readlines():
#         word_list += re.findall(r'\b(\w{16})\b', line)


# print(word_list)