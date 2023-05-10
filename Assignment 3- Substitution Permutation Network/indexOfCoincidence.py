file1 = open("test.txt", "r") #Input file containing the cipher text
ciphertxt = file1.read() 

print(ciphertxt)

freqs = [[0, chr(ord('a')+i)] for i in range(0, 26)] #mapping of the characters to their frequencies

print(freqs)

for c in ciphertxt:
    if not((ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122)):
        continue
    if ord(c)<=90: #make all the letters lowercase
        c = chr(ord(c) + 32)
    index = ord(c)-ord('a')
    # print(index)
    freqs[index][0] += 1

freqs.sort() #sort on the basis of frequency
print(freqs)

total = 0
for it in freqs:
    total += it[0]
print(total)

ans=0
for it in freqs:
    ans += (it[0]/total)**2
print(ans)