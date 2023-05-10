file1 = open("test.txt", "r")
file2 = open("plain.txt", "a")
ciphertxt = file1.read()

print(ciphertxt)

freqs = [[0, i] for i in range(0, 26)]

print(freqs)

for c in ciphertxt:
    if not((ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122)):
        continue
    if ord(c)<=90:
        c = chr(ord(c) + 32)
    index = ord(c)-ord('a')
    print(index)
    freqs[index][0] += 1

freqs.sort()
print(freqs)